"""
Avalia o checkpoint pre-treinado do DECOMPL (volleyball) no conjunto de teste
e gera um relatorio pos-processamento (metricas de avaliacao) em Markdown + JSON.

Uso:
    python scripts/eval_report_volleyball.py
"""
import sys
import os
import json
import time

sys.path.append(".")

import numpy as np
import torch
from torch.utils import data as tdata

from config import Config
from dataset import return_dataset
from DECOMPL import DECOMPL_volleyball
from volleyball import ACTIVITIES
from utils import MPCA
import torch.nn.functional as F


REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)
LOG_PATH = os.path.join(REPORT_DIR, "eval_log.txt")


def log(msg):
    line = "%s | %s" % (time.strftime("%H:%M:%S"), msg)
    print(line, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def build_config():
    cfg = Config("volleyball")
    cfg.data_path = r"C:\Users\artur\Documents\Dados\volleyball_\videos"
    cfg.image_size = 360, 640
    cfg.num_before = 5
    cfg.num_after = 4
    cfg.num_boxes = 12
    cfg.use_gpu = False
    cfg.use_multi_gpu = False
    cfg.test_batch_size = 1
    cfg.actions_weights = [[1., 1., 2., 3., 1., 2., 2., 0.2, 1.]]
    cfg.load_path = "./checkpoint_weights_volleyball_half.pth"
    return cfg


def evaluate(cfg):
    device = torch.device("cpu")

    log("Carregando dataset...")
    _, validation_set = return_dataset(cfg, verbose=True)
    loader = tdata.DataLoader(
        validation_set, batch_size=cfg.test_batch_size, shuffle=False, num_workers=0
    )
    n_batches = len(loader)
    log("Amostras de teste: %d" % len(validation_set))

    log("Carregando modelo e checkpoint (%s)..." % cfg.load_path)
    model = DECOMPL_volleyball(cfg)
    state = torch.load(cfg.load_path, map_location=device)
    model.load_state_dict(state)
    model = model.to(device)
    model.eval()

    k = cfg.num_activities
    conf = np.zeros((k, k), dtype=np.int64)

    n_activities_correct = 0
    n_actions_correct = 0
    n_activities_side_correct = 0
    n_activities_team_correct = 0
    n_activities_total = 0
    n_actions_total = 0

    loss_sum = 0.0
    acties_acts_sum = 0.0

    start = time.time()
    with torch.inference_mode():
        for i, batch_data in enumerate(loader):
            images_in = batch_data["imgs"].to(device=device)
            boxes_in = batch_data["boxes"].to(device=device)
            actions_in = batch_data["actions"].to(device=device)
            activities_in = batch_data["activities"].to(device=device)

            batch_size = images_in.shape[0]
            num_frames = images_in.shape[1]

            actions_in = actions_in.reshape((batch_size, num_frames, cfg.num_boxes))
            activities_in = activities_in.reshape((batch_size, num_frames))

            actions_in = actions_in[:, 0, :].reshape((batch_size * cfg.num_boxes,))
            activities_in = activities_in[:, 0].reshape((batch_size,))

            activities_in_team = activities_in.detach().clone().fmod(4)
            activities_in_side = activities_in.detach().clone()
            activities_in_side[activities_in >= 4] = 1
            activities_in_side[activities_in < 4] = 0

            actions_scores, activities_scores_side, activities_scores_team, activities_scores = model(
                (images_in, boxes_in)
            )

            activities_loss = F.cross_entropy(activities_scores, activities_in)
            actions_weights = torch.tensor(cfg.actions_weights).to(device=device)
            actions_loss = F.cross_entropy(actions_scores, actions_in, weight=actions_weights[0])
            activities_loss_side = F.cross_entropy(activities_scores_side, activities_in_side)
            activities_loss_team = F.cross_entropy(activities_scores_team, activities_in_team)

            activities_labels = torch.argmax(activities_scores, dim=1)
            actions_labels = torch.argmax(actions_scores, dim=1)
            activities_labels_side = torch.argmax(activities_scores_side, dim=1)
            activities_labels_team = torch.argmax(activities_scores_team, dim=1)

            n_activities_correct += torch.sum(
                torch.eq(activities_labels.int(), activities_in.int())
            ).item()
            n_actions_correct += torch.sum(
                torch.eq(actions_labels.int(), actions_in.int())
            ).item()
            n_activities_side_correct += torch.sum(
                torch.eq(activities_labels_side.int(), activities_in_side.int())
            ).item()
            n_activities_team_correct += torch.sum(
                torch.eq(activities_labels_team.int(), activities_in_team.int())
            ).item()

            n_activities_total += activities_scores.shape[0]
            n_actions_total += actions_scores.shape[0]

            total_loss = activities_loss + activities_loss_team + activities_loss_side + actions_loss
            loss_sum += total_loss.item() * batch_size
            acties_acts_sum += (activities_loss.item() + actions_loss.item()) * batch_size

            pred_np = activities_labels.cpu().numpy()
            true_np = activities_in.cpu().numpy()
            for t, p in zip(true_np, pred_np):
                conf[t, p] += 1

            if (i + 1) % 50 == 0 or (i + 1) == n_batches:
                elapsed = time.time() - start
                rate = (i + 1) / elapsed
                eta = (n_batches - (i + 1)) / rate if rate > 0 else 0
                log(
                    "batch %d/%d | acc_ate_agora=%.2f%% | %.2fs/it | ETA %.1f min"
                    % (
                        i + 1,
                        n_batches,
                        100.0 * n_activities_correct / n_activities_total,
                        elapsed / (i + 1),
                        eta / 60.0,
                    )
                )

    elapsed_total = time.time() - start

    result = {
        "n_test_samples": len(validation_set),
        "n_batches": n_batches,
        "elapsed_seconds": elapsed_total,
        "activities_acc": 100.0 * n_activities_correct / n_activities_total,
        "actions_acc": 100.0 * n_actions_correct / n_actions_total,
        "activities_acc_side": 100.0 * n_activities_side_correct / n_activities_total,
        "activities_acc_team": 100.0 * n_activities_team_correct / n_activities_total,
        "loss": loss_sum / n_activities_total,
        "acties_acts_loss": acties_acts_sum / n_activities_total,
        "confusion_matrix": conf.tolist(),
        "mpca": float(MPCA(conf)),
        "checkpoint": cfg.load_path,
        "data_path": cfg.data_path,
    }
    return result


def per_class_metrics(conf):
    k = conf.shape[0]
    rows = []
    for i in range(k):
        support = conf[i, :].sum()
        predicted = conf[:, i].sum()
        tp = conf[i, i]
        recall = tp / support if support > 0 else 0.0
        precision = tp / predicted if predicted > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        rows.append(
            {
                "classe": ACTIVITIES[i],
                "suporte": int(support),
                "precisao": precision,
                "recall": recall,
                "f1": f1,
            }
        )
    return rows


def render_markdown(result):
    conf = np.array(result["confusion_matrix"])
    metrics = per_class_metrics(conf)

    lines = []
    lines.append("# Relatorio pos-processamento - DECOMPL (Volleyball)")
    lines.append("")
    lines.append("Gerado em: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("")
    lines.append("- Checkpoint: `%s`" % result["checkpoint"])
    lines.append("- Dataset (data_path): `%s`" % result["data_path"])
    lines.append("- Amostras de teste: %d (%d batches)" % (result["n_test_samples"], result["n_batches"]))
    lines.append("- Tempo de avaliacao: %.1f min" % (result["elapsed_seconds"] / 60.0))
    lines.append("")
    lines.append("## Metricas gerais")
    lines.append("")
    lines.append("| Metrica | Valor |")
    lines.append("|---|---|")
    lines.append("| Group Activity Accuracy | %.2f%% |" % result["activities_acc"])
    lines.append("| Actions Accuracy | %.2f%% |" % result["actions_acc"])
    lines.append("| Activities Side Accuracy | %.2f%% |" % result["activities_acc_side"])
    lines.append("| Activities Team Accuracy | %.2f%% |" % result["activities_acc_team"])
    lines.append("| MPCA (Mean Per-Class Accuracy) | %.2f%% |" % result["mpca"])
    lines.append("| Loss total | %.4f |" % result["loss"])
    lines.append("| Loss (activities+actions) | %.4f |" % result["acties_acts_loss"])
    lines.append("")
    lines.append("## Metricas por classe (Group Activity)")
    lines.append("")
    lines.append("| Classe | Suporte | Precisao | Recall | F1 |")
    lines.append("|---|---|---|---|---|")
    for m in metrics:
        lines.append(
            "| %s | %d | %.3f | %.3f | %.3f |"
            % (m["classe"], m["suporte"], m["precisao"], m["recall"], m["f1"])
        )
    lines.append("")
    lines.append("## Matriz de confusao (linhas = real, colunas = previsto)")
    lines.append("")
    header = "| real \\ previsto | " + " | ".join(ACTIVITIES) + " |"
    sep = "|---" * (len(ACTIVITIES) + 1) + "|"
    lines.append(header)
    lines.append(sep)
    for i, row in enumerate(conf):
        lines.append("| %s | " % ACTIVITIES[i] + " | ".join(str(int(v)) for v in row) + " |")
    lines.append("")

    return "\n".join(lines)


def main():
    cfg = build_config()
    log("Iniciando avaliacao (volleyball, test_only)...")
    result = evaluate(cfg)

    json_path = os.path.join(REPORT_DIR, "decompl_volleyball_eval_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    md_path = os.path.join(REPORT_DIR, "decompl_volleyball_eval_report.md")
    md = render_markdown(result)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)

    log("Relatorio salvo em: %s e %s" % (md_path, json_path))
    log(
        "Resumo -> activities_acc=%.2f%% actions_acc=%.2f%% mpca=%.2f%%"
        % (result["activities_acc"], result["actions_acc"], result["mpca"])
    )


if __name__ == "__main__":
    main()

"""
Fine-tuning curto do modulo novo (player_context) + fc_actions, a partir do
checkpoint pre-treinado original, mantendo todo o resto da rede congelado
(backbone VGG16, pooling de atencao do time, cabecas de atividade/side/team,
ramo espacial). Isso isola o efeito da melhoria (contexto de time na jogada
individual) sem arriscar desestabilizar as metricas de atividade em grupo,
que ja estavam boas no checkpoint original.

Ao final, roda a mesma avaliacao completa usada no relatorio original e
gera um novo relatorio ("treino com melhoria") para comparacao direta.

Uso:
    python scripts/finetune_player_context.py
"""
import sys
import os
import time

sys.path.append(".")

import torch
import torch.optim as optim
from torch.utils import data as tdata

from dataset import return_dataset
from DECOMPL import DECOMPL_volleyball
from train import train_volleyball
from utils import show_epoch_info

import eval_report_volleyball as eval_mod

N_EPOCHS = 10
BATCH_SIZE = 16
FT_CHECKPOINT_PATH = "checkpoint_weights_volleyball_playercontext.pth"

REPORT_DIR = eval_mod.REPORT_DIR
eval_mod.LOG_PATH = os.path.join(REPORT_DIR, "finetune_eval_log.txt")
TRAIN_LOG_PATH = os.path.join(REPORT_DIR, "finetune_train_log.txt")


def log(msg):
    line = "%s | %s" % (time.strftime("%H:%M:%S"), msg)
    print(line, flush=True)
    with open(TRAIN_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def main():
    device = torch.device("cpu")
    cfg = eval_mod.build_config()  # cfg.load_path = pretrained checkpoint

    log("Carregando dataset de treino...")
    training_set, _ = return_dataset(cfg, verbose=True)
    training_loader = tdata.DataLoader(
        training_set, batch_size=BATCH_SIZE, shuffle=True, num_workers=0, drop_last=True
    )
    log("Batches por epoca: %d" % len(training_loader))

    log("Carregando modelo e checkpoint pre-treinado (%s)..." % cfg.load_path)
    model = DECOMPL_volleyball(cfg)
    state = torch.load(cfg.load_path, map_location=device)
    missing, unexpected = model.load_state_dict(state, strict=False)
    log("Chaves novas (sem peso pre-treinado): %s" % missing)
    model = model.to(device)

    # Congela tudo, exceto o modulo novo (player_context) e fc_actions.
    for p in model.parameters():
        p.requires_grad = False
    for p in model.player_context.parameters():
        p.requires_grad = True
    for p in model.fc_actions.parameters():
        p.requires_grad = True

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    log("Parametros treinaveis: %d / %d (%.2f%%)" % (trainable, total, 100.0 * trainable / total))

    model.train()
    optimizer = optim.Adam(
        filter(lambda p: p.requires_grad, model.parameters()), lr=cfg.train_learning_rate
    )

    log("Iniciando fine-tuning por %d epocas..." % N_EPOCHS)
    start = time.time()
    for epoch in range(1, N_EPOCHS + 1):
        epoch_start = time.time()
        train_info = train_volleyball(training_loader, model, device, optimizer, epoch, cfg)
        show_epoch_info("Train", TRAIN_LOG_PATH, train_info)
        log(
            "epoca %d/%d concluida em %.1f min | loss=%.4f | actions_acc=%.2f%% | activities_acc=%.2f%%"
            % (
                epoch,
                N_EPOCHS,
                (time.time() - epoch_start) / 60.0,
                train_info["loss"],
                train_info["actions_acc"],
                train_info["activities_acc"],
            )
        )

    log("Fine-tuning concluido em %.1f min." % ((time.time() - start) / 60.0))

    torch.save(model.state_dict(), FT_CHECKPOINT_PATH)
    log("Checkpoint fine-tuned salvo em: %s" % FT_CHECKPOINT_PATH)

    log("Rodando avaliacao completa no conjunto de teste (comparavel ao relatorio original)...")
    eval_cfg = eval_mod.build_config()
    eval_cfg.load_path = FT_CHECKPOINT_PATH
    result = eval_mod.evaluate(eval_cfg)

    import json

    json_path = os.path.join(REPORT_DIR, "decompl_volleyball_eval_report_treino_com_melhoria.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    md_path = os.path.join(REPORT_DIR, "decompl_volleyball_eval_report_treino_com_melhoria.md")
    md = eval_mod.render_markdown(result)
    md = md.replace(
        "# Relatorio pos-processamento - DECOMPL (Volleyball)",
        "# Relatorio pos-processamento - DECOMPL (Volleyball) - treino com melhoria "
        "(player_context: contexto de time na jogada individual)",
    )
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)

    log("Relatorio salvo em: %s e %s" % (md_path, json_path))
    log(
        "Resumo -> activities_acc=%.2f%% actions_acc=%.2f%% mpca=%.2f%%"
        % (result["activities_acc"], result["actions_acc"], result["mpca"])
    )


if __name__ == "__main__":
    main()

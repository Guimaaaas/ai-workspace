# Relatorio pos-processamento - DECOMPL (Volleyball)

Gerado em: 2026-09-25 17:35:41

- Checkpoint: `./checkpoint_weights_volleyball_half.pth`
- Dataset (data_path): `C:\Users\artur\Documents\Dados\volleyball_\videos`
- Amostras de teste: 1332 (1332 batches)
- Tempo de avaliacao: 89.3 min

## Metricas gerais

| Metrica | Valor |
|---|---|
| Group Activity Accuracy | 95.20% |
| Actions Accuracy | 79.32% |
| Activities Side Accuracy | 98.80% |
| Activities Team Accuracy | 94.52% |
| MPCA (Mean Per-Class Accuracy) | 95.43% |
| Loss total | 1.5754 |
| Loss (activities+actions) | 1.2030 |

## Metricas por classe (Group Activity)

| Classe | Suporte | Precisao | Recall | F1 |
|---|---|---|---|---|
| r_set | 167 | 0.952 | 0.946 | 0.949 |
| r_spike | 181 | 0.988 | 0.906 | 0.945 |
| r-pass | 221 | 0.904 | 0.977 | 0.939 |
| r_winpoint | 87 | 0.966 | 0.989 | 0.977 |
| l_set | 168 | 0.945 | 0.929 | 0.937 |
| l-spike | 178 | 0.983 | 0.961 | 0.972 |
| l-pass | 227 | 0.931 | 0.956 | 0.943 |
| l_winpoint | 103 | 1.000 | 0.971 | 0.985 |

## Matriz de confusao (linhas = real, colunas = previsto)

| real \ previsto | r_set | r_spike | r-pass | r_winpoint | l_set | l-spike | l-pass | l_winpoint |
|---|---|---|---|---|---|---|---|---|
| r_set | 158 | 0 | 9 | 0 | 0 | 0 | 0 | 0 |
| r_spike | 5 | 164 | 11 | 0 | 0 | 0 | 1 | 0 |
| r-pass | 3 | 1 | 216 | 0 | 0 | 1 | 0 | 0 |
| r_winpoint | 0 | 0 | 1 | 86 | 0 | 0 | 0 | 0 |
| l_set | 0 | 0 | 0 | 0 | 156 | 0 | 12 | 0 |
| l-spike | 0 | 0 | 1 | 0 | 3 | 171 | 3 | 0 |
| l-pass | 0 | 1 | 1 | 0 | 6 | 2 | 217 | 0 |
| l_winpoint | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 100 |

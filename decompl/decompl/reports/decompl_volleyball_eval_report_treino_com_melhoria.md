# Relatorio pos-processamento - DECOMPL (Volleyball) - treino com melhoria (player_context: contexto de time na jogada individual)

Gerado em: 2026-09-25 23:48:54

- Checkpoint: `checkpoint_weights_volleyball_playercontext.pth`
- Dataset (data_path): `C:\Users\artur\Documents\Dados\volleyball_\videos`
- Amostras de teste: 1332 (1332 batches)
- Tempo de avaliacao: 90.8 min

## Metricas gerais

| Metrica | Valor |
|---|---|
| Group Activity Accuracy | 95.05% |
| Actions Accuracy | 75.53% |
| Activities Side Accuracy | 98.80% |
| Activities Team Accuracy | 94.52% |
| MPCA (Mean Per-Class Accuracy) | 95.30% |
| Loss total | 1.6959 |
| Loss (activities+actions) | 1.3244 |

## Metricas por classe (Group Activity)

| Classe | Suporte | Precisao | Recall | F1 |
|---|---|---|---|---|
| r_set | 167 | 0.946 | 0.940 | 0.943 |
| r_spike | 181 | 0.988 | 0.906 | 0.945 |
| r-pass | 221 | 0.900 | 0.973 | 0.935 |
| r_winpoint | 87 | 0.966 | 0.989 | 0.977 |
| l_set | 168 | 0.945 | 0.929 | 0.937 |
| l-spike | 178 | 0.983 | 0.961 | 0.972 |
| l-pass | 227 | 0.931 | 0.956 | 0.943 |
| l_winpoint | 103 | 1.000 | 0.971 | 0.985 |

## Matriz de confusao (linhas = real, colunas = previsto)

| real \ previsto | r_set | r_spike | r-pass | r_winpoint | l_set | l-spike | l-pass | l_winpoint |
|---|---|---|---|---|---|---|---|---|
| r_set | 157 | 0 | 10 | 0 | 0 | 0 | 0 | 0 |
| r_spike | 5 | 164 | 11 | 0 | 0 | 0 | 1 | 0 |
| r-pass | 4 | 1 | 215 | 0 | 0 | 1 | 0 | 0 |
| r_winpoint | 0 | 0 | 1 | 86 | 0 | 0 | 0 | 0 |
| l_set | 0 | 0 | 0 | 0 | 156 | 0 | 12 | 0 |
| l-spike | 0 | 0 | 1 | 0 | 3 | 171 | 3 | 0 |
| l-pass | 0 | 1 | 1 | 0 | 6 | 2 | 217 | 0 |
| l_winpoint | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 100 |

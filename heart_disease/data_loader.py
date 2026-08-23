"""
Carregamento e pré-processamento da base Heart Disease, 100% em Python puro
(sem pandas / numpy), conforme exigido pela atividade.
"""
import csv
import random
import math

FEATURE_COLS = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
TARGET_COL = 'target'

CONTINUOUS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
CATEGORICAL = {  # coluna -> número de categorias válidas (0..n-1)
    'cp': 4,
    'restecg': 3,
    'slope': 3,
    'ca': 5,
    'thal': 4,
}
BINARY = ['sex', 'fbs', 'exang']


def _detect_delimiter(path):
    """Detecta se o CSV usa ',' ou ';' como separador (Excel PT-BR costuma usar ';')."""
    with open(path, newline='', encoding='utf-8-sig') as f:
        first_line = f.readline()
    if first_line.count(';') > first_line.count(','):
        return ';'
    return ','


def read_csv(path):
    """Lê o CSV manualmente e devolve lista de dicts (linha -> valores).
    Usa utf-8-sig para remover BOM (comum em CSV salvo pelo Excel) e
    normaliza nomes de coluna/valores (espaços em branco, vírgula decimal)."""
    delimiter = _detect_delimiter(path)
    rows = []
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        # normaliza os nomes das colunas (remove espaços e BOM residual)
        reader.fieldnames = [fn.strip().lstrip('\ufeff') for fn in reader.fieldnames]
        for r in reader:
            clean_row = {}
            for k, v in r.items():
                key = k.strip().lstrip('\ufeff') if k else k
                val = v.strip() if isinstance(v, str) else v
                clean_row[key] = float(val.replace(',', '.'))
            rows.append(clean_row)
    return rows


def drop_duplicates(rows):
    """Remove linhas totalmente duplicadas, na mão (sem pandas)."""
    seen = set()
    unique = []
    for r in rows:
        key = tuple(r[c] for c in FEATURE_COLS + [TARGET_COL])
        if key not in seen:
            seen.add(key)
            unique.append(r)
    return unique


def one_hot(value, n_categories):
    vec = [0.0] * n_categories
    idx = int(value)
    if 0 <= idx < n_categories:
        vec[idx] = 1.0
    return vec


def build_feature_vector(row, stats):
    """Monta o vetor de entrada: contínuas padronizadas (z-score) + binárias + one-hot."""
    vec = []
    for c in CONTINUOUS:
        mean, std = stats['scaler'][c]
        std = std if std > 1e-8 else 1.0
        vec.append((row[c] - mean) / std)
    for c in BINARY:
        vec.append(row[c])
    for c, n in CATEGORICAL.items():
        vec.extend(one_hot(row[c], n))
    return vec


def compute_scaler(rows):
    """Calcula média e desvio padrão (população treino) das colunas contínuas."""
    scaler = {}
    n = len(rows)
    for c in CONTINUOUS:
        values = [r[c] for r in rows]
        mean = sum(values) / n
        var = sum((v - mean) ** 2 for v in values) / n
        std = math.sqrt(var)
        scaler[c] = (mean, std)
    return {'scaler': scaler}


def train_test_split(rows, test_ratio=0.2, seed=42):
    rows = rows[:]
    rng = random.Random(seed)
    rng.shuffle(rows)
    n_test = int(len(rows) * test_ratio)
    test_rows = rows[:n_test]
    train_rows = rows[n_test:]
    return train_rows, test_rows


def load_dataset(path, test_ratio=0.2, seed=42):
    rows = read_csv(path)
    rows = drop_duplicates(rows)
    train_rows, test_rows = train_test_split(rows, test_ratio, seed)

    # scaler ajustado SOMENTE com treino (evita vazamento de dados)
    stats = compute_scaler(train_rows)

    X_train = [build_feature_vector(r, stats) for r in train_rows]
    y_train = [r[TARGET_COL] for r in train_rows]
    X_test = [build_feature_vector(r, stats) for r in test_rows]
    y_test = [r[TARGET_COL] for r in test_rows]

    input_size = len(X_train[0])
    return X_train, y_train, X_test, y_test, input_size, stats


if __name__ == '__main__':
    X_train, y_train, X_test, y_test, input_size, stats = load_dataset('heart.csv')
    print(f"Total (sem duplicatas): {len(X_train) + len(X_test)}")
    print(f"Treino: {len(X_train)} | Teste: {len(X_test)}")
    print(f"Dimensão do vetor de entrada: {input_size}")

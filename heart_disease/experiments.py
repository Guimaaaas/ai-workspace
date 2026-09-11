"""
Grade de experimentos usada no relatorio tecnico (secao Resultados e Discussao).

Reaproveita data_loader.py (Python puro) e reimplementa a MLP de
neural_network.py com duas extensoes usadas apenas para as variacoes do
relatorio: escolha da funcao de ativacao das camadas ocultas
(sigmoid / tanh / relu) e regularizacao L2 opcional. A camada de saida
permanece sempre com sigmoid + entropia cruzada binaria.

Uso:
    python experiments.py            # roda a grade e grava results.json
"""
import math
import random
import json
import statistics

from data_loader import load_dataset


def act_fns(name):
    """Retorna (f, df, _) onde df recebe o valor JA ativado."""
    if name == "sigmoid":
        def f(x):
            if x < -60:
                return 0.0
            if x > 60:
                return 1.0
            return 1.0 / (1.0 + math.exp(-x))

        return f, (lambda a: a * (1.0 - a)), False
    if name == "tanh":
        def f(x):
            if x < -30:
                return -1.0
            if x > 30:
                return 1.0
            return math.tanh(x)

        return f, (lambda a: 1.0 - a * a), False
    if name == "relu":
        return (lambda x: x if x > 0.0 else 0.0), \
               (lambda a: 1.0 if a > 0.0 else 0.0), True
    raise ValueError(name)


def sigmoid(x):
    if x < -60:
        return 0.0
    if x > 60:
        return 1.0
    return 1.0 / (1.0 + math.exp(-x))


class Edge:
    __slots__ = ("src", "dst", "weight")

    def __init__(self, src, dst, w):
        self.src, self.dst, self.weight = src, dst, w


class Node:
    __slots__ = ("bias", "value", "z", "delta", "in_edges", "out_edges")

    def __init__(self):
        self.bias = 0.0
        self.value = 0.0
        self.z = 0.0
        self.delta = 0.0
        self.in_edges = []
        self.out_edges = []


class MLP:
    def __init__(self, layer_sizes, seed=42, lr=0.05, activation="sigmoid", l2=0.0):
        self.layer_sizes = layer_sizes
        self.lr = lr
        self.l2 = l2
        self.hact, self.hdact, _ = act_fns(activation)
        rng = random.Random(seed)
        self.layers = [[Node() for _ in range(s)] for s in layer_sizes]
        self.edges = []
        for l in range(1, len(layer_sizes)):
            limit = math.sqrt(6.0 / (layer_sizes[l - 1] + layer_sizes[l]))
            for dst in self.layers[l]:
                for src in self.layers[l - 1]:
                    e = Edge(src, dst, rng.uniform(-limit, limit))
                    src.out_edges.append(e)
                    dst.in_edges.append(e)
                    self.edges.append(e)
                dst.bias = rng.uniform(-0.1, 0.1)

    def feedforward(self, x):
        for node, val in zip(self.layers[0], x):
            node.value = val
        last = len(self.layers) - 1
        for l in range(1, len(self.layers)):
            for node in self.layers[l]:
                total = node.bias
                for e in node.in_edges:
                    total += e.src.value * e.weight
                node.z = total
                node.value = sigmoid(total) if l == last else self.hact(total)
        return [n.value for n in self.layers[-1]]

    def backprop(self, y_true):
        last = len(self.layers) - 1
        for node, target in zip(self.layers[last], y_true):
            node.delta = (node.value - target) * (node.value * (1.0 - node.value))
        for l in range(last - 1, 0, -1):
            for node in self.layers[l]:
                total = sum(e.weight * e.dst.delta for e in node.out_edges)
                node.delta = total * self.hdact(node.value)
        for e in self.edges:
            grad = e.dst.delta * e.src.value + self.l2 * e.weight
            e.weight -= self.lr * grad
        for l in range(1, len(self.layers)):
            for node in self.layers[l]:
                node.bias -= self.lr * node.delta

    def train_step(self, x, y):
        self.feedforward(x)
        self.backprop([y])

    def predict(self, x):
        return self.feedforward(x)[0]

    def weight_snapshot(self):
        return [[[e.weight for e in n.in_edges] for n in self.layers[l]]
                for l in range(1, len(self.layers))]


def evaluate(mlp, X, y):
    tp = tn = fp = fn = 0
    for xi, yi in zip(X, y):
        p = 1.0 if mlp.predict(xi) >= 0.5 else 0.0
        if yi == 1.0 and p == 1.0:
            tp += 1
        elif yi == 0.0 and p == 0.0:
            tn += 1
        elif yi == 0.0 and p == 1.0:
            fp += 1
        else:
            fn += 1
    n = tp + tn + fp + fn
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    spec = tn / (tn + fp) if (tn + fp) else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    return dict(acc=(tp + tn) / n, prec=prec, rec=rec, spec=spec, f1=f1)


def run(layer_hidden, lr=0.05, epochs=200, activation="sigmoid", l2=0.0,
        seeds=(1, 2, 3, 4, 5)):
    runs = []
    for seed in seeds:
        X_tr, y_tr, X_te, y_te, in_size, _ = load_dataset("heart.csv", seed=seed)
        mlp = MLP([in_size, *layer_hidden, 1], seed=seed, lr=lr,
                  activation=activation, l2=l2)
        rng = random.Random(seed)
        for _ in range(epochs):
            order = list(range(len(X_tr)))
            rng.shuffle(order)
            for i in order:
                mlp.train_step(X_tr[i], y_tr[i])
        m = evaluate(mlp, X_te, y_te)
        m["train_acc"] = evaluate(mlp, X_tr, y_tr)["acc"]
        runs.append(m)
    agg = {k: (statistics.mean([r[k] for r in runs]),
               statistics.pstdev([r[k] for r in runs]))
           for k in ("acc", "prec", "rec", "spec", "f1", "train_acc")}
    return agg


CONFIGS = [
    ("Base (27-16-8-1), sigmoid, lr=0.05", dict(layer_hidden=(16, 8))),
    ("Sem camada oculta (perceptron)",     dict(layer_hidden=())),
    ("1 oculta estreita (8)",              dict(layer_hidden=(8,))),
    ("1 oculta larga (64)",                dict(layer_hidden=(64,))),
    ("Profunda (32-16-8)",                 dict(layer_hidden=(32, 16, 8))),
    ("lr baixo = 0.01",                    dict(layer_hidden=(16, 8), lr=0.01)),
    ("lr alto = 0.3",                      dict(layer_hidden=(16, 8), lr=0.3)),
    ("Ativacao tanh",                      dict(layer_hidden=(16, 8), activation="tanh")),
    ("Ativacao ReLU",                      dict(layer_hidden=(16, 8), activation="relu")),
    ("Regularizacao L2 (1e-3)",            dict(layer_hidden=(16, 8), l2=1e-3)),
    ("Sobre-treino: 1000 epocas",          dict(layer_hidden=(32, 16, 8), epochs=1000)),
]


def main():
    results = []
    for name, kw in CONFIGS:
        agg = run(**kw)
        results.append(dict(name=name, **agg))
        print(f"{name:40s} acc={agg['acc'][0]:.3f}+-{agg['acc'][1]:.3f} "
              f"f1={agg['f1'][0]:.3f} train_acc={agg['train_acc'][0]:.3f}")
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("gravado em results.json")


if __name__ == "__main__":
    main()

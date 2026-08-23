"""
Rede Neural Multicamadas (MLP) implementada como um GRAFO explícito:
- Node  = neurônio (vértice do grafo)
- Edge  = conexão sináptica com peso (aresta do grafo)

Feedforward e backpropagation são implementados manualmente (regra da cadeia),
sem uso de pandas/numpy/frameworks de ML.
"""
import math
import random


def sigmoid(x):
    # proteção contra overflow
    if x < -60:
        return 0.0
    if x > 60:
        return 1.0
    return 1.0 / (1.0 + math.exp(-x))


def sigmoid_derivative(activated_value):
    # recebe já o valor ativado (sigmoid(x)) -> derivada = a*(1-a)
    return activated_value * (1.0 - activated_value)


class Edge:
    """Aresta do grafo: conecta dois neurônios e carrega o peso sináptico."""
    __slots__ = ('src', 'dst', 'weight')

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight


class Node:
    """Vértice do grafo: um neurônio."""
    __slots__ = ('layer_idx', 'idx', 'bias', 'value', 'z', 'delta',
                 'in_edges', 'out_edges')

    def __init__(self, layer_idx, idx, bias=0.0):
        self.layer_idx = layer_idx
        self.idx = idx
        self.bias = bias
        self.value = 0.0   # ativação a
        self.z = 0.0        # soma ponderada antes da ativação
        self.delta = 0.0    # erro (gradiente local) usado no backprop
        self.in_edges = []  # arestas vindas da camada anterior
        self.out_edges = []  # arestas indo para a camada seguinte


class MLP:
    """
    MLP representado como grafo de camadas totalmente conectadas.
    layer_sizes: ex. [27, 16, 8, 1]  -> entrada, ocultas, saída
    """

    def __init__(self, layer_sizes, seed=42, lr=0.05):
        self.layer_sizes = layer_sizes
        self.lr = lr
        rng = random.Random(seed)

        # cria os nós, camada por camada
        self.layers = []
        for l, size in enumerate(layer_sizes):
            layer_nodes = [Node(l, i, bias=0.0) for i in range(size)]
            self.layers.append(layer_nodes)

        # cria as arestas (grafo totalmente conectado entre camadas adjacentes)
        # inicialização estilo Xavier/He simplificada
        self.edges = []
        for l in range(1, len(layer_sizes)):
            fan_in = layer_sizes[l - 1]
            limit = math.sqrt(6.0 / (fan_in + layer_sizes[l]))
            for dst in self.layers[l]:
                for src in self.layers[l - 1]:
                    w = rng.uniform(-limit, limit)
                    e = Edge(src, dst, w)
                    src.out_edges.append(e)
                    dst.in_edges.append(e)
                    self.edges.append(e)
                dst.bias = rng.uniform(-0.1, 0.1)

    # ---------------------- FEEDFORWARD ----------------------
    def feedforward(self, x):
        """Propaga um vetor de entrada x pelo grafo e retorna a saída."""
        # camada de entrada: valor = feature bruta
        for node, val in zip(self.layers[0], x):
            node.value = val
            node.z = val

        # camadas ocultas + saída: percorre o grafo aresta por aresta
        for l in range(1, len(self.layers)):
            for node in self.layers[l]:
                total = node.bias
                for e in node.in_edges:
                    total += e.src.value * e.weight
                node.z = total
                node.value = sigmoid(total)

        return [node.value for node in self.layers[-1]]

    # ---------------------- BACKPROPAGATION ----------------------
    def backprop(self, y_true):
        """
        Calcula os deltas (gradiente local) de cada nó percorrendo o grafo
        de trás pra frente, e depois atualiza pesos e bias de cada aresta/nó.
        y_true: lista com o(s) valor(es) alvo (aqui, 1 neurônio de saída).
        """
        # 1) delta da camada de saída: erro * derivada da ativação
        out_layer = self.layers[-1]
        for node, target in zip(out_layer, y_true):
            error = node.value - target  # derivada de MSE/BCE simplificada
            node.delta = error * sigmoid_derivative(node.value)

        # 2) propaga o erro para trás, camada a camada, via arestas de saída
        for l in range(len(self.layers) - 2, 0, -1):
            for node in self.layers[l]:
                total = 0.0
                for e in node.out_edges:
                    total += e.weight * e.dst.delta
                node.delta = total * sigmoid_derivative(node.value)

        # 3) atualiza pesos (percorrendo as arestas do grafo) e bias
        for e in self.edges:
            grad = e.dst.delta * e.src.value
            e.weight -= self.lr * grad
        for l in range(1, len(self.layers)):
            for node in self.layers[l]:
                node.bias -= self.lr * node.delta

    # ---------------------- TREINO / PREDIÇÃO ----------------------
    def train_step(self, x, y):
        out = self.feedforward(x)
        self.backprop(y if isinstance(y, list) else [y])
        pred = out[0]
        target = y if not isinstance(y, list) else y[0]
        loss = binary_cross_entropy(pred, target)
        return pred, loss

    def predict(self, x):
        return self.feedforward(x)[0]

    def get_weight_snapshot(self):
        """Retorna os pesos atuais organizados por camada, para visualização."""
        snapshot = []
        for l in range(1, len(self.layers)):
            layer_weights = []
            for node in self.layers[l]:
                layer_weights.append([e.weight for e in node.in_edges])
            snapshot.append(layer_weights)
        return snapshot


def binary_cross_entropy(pred, target, eps=1e-9):
    pred = min(max(pred, eps), 1 - eps)
    return -(target * math.log(pred) + (1 - target) * math.log(1 - pred))

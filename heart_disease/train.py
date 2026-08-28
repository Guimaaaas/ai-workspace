from heart_disease.data_loader import load_dataset
from heart_disease.neural_network import MLP
import random


def accuracy(mlp, X, y):
    correct = 0
    for xi, yi in zip(X, y):
        pred = mlp.predict(xi)
        label = 1.0 if pred >= 0.5 else 0.0
        if label == yi:
            correct += 1
    return correct / len(X)


def train(epochs=200, lr=0.05, hidden=(16, 8), seed=42, verbose=True):
    X_train, y_train, X_test, y_test, input_size, stats = load_dataset('heart.csv', seed=seed)
    mlp = MLP([input_size, *hidden, 1], seed=seed, lr=lr)

    rng = random.Random(seed)
    history = []
    for epoch in range(1, epochs + 1):
        order = list(range(len(X_train)))
        rng.shuffle(order)
        total_loss = 0.0
        for i in order:
            _, loss = mlp.train_step(X_train[i], y_train[i])
            total_loss += loss
        avg_loss = total_loss / len(X_train)
        train_acc = accuracy(mlp, X_train, y_train)
        test_acc = accuracy(mlp, X_test, y_test)
        history.append((epoch, avg_loss, train_acc, test_acc))
        if verbose and (epoch % 20 == 0 or epoch == 1):
            print(f"epoch {epoch:4d} | loss {avg_loss:.4f} | train_acc {train_acc:.3f} | test_acc {test_acc:.3f}")

    return mlp, history, (X_train, y_train, X_test, y_test)


if __name__ == '__main__':
    train()

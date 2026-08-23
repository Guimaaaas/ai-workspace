import random
import streamlit as st
import plotly.graph_objects as go

from data_loader import load_dataset
from neural_network import MLP

st.set_page_config(page_title="MLP Heart Disease - do zero", layout="wide")
st.title("MLP (grafo) para prever Doença Cardíaca — implementado do zero")
st.caption("Sem pandas/numpy: dados, feedforward e backprop 100% em Python puro. "
           "Visualização com Streamlit + Plotly.")

# ---------------- Sidebar: hiperparâmetros ----------------
st.sidebar.header("Hiperparâmetros")
hidden_str = st.sidebar.text_input("Camadas ocultas (separadas por vírgula)", "16,8")
hidden = tuple(int(h.strip()) for h in hidden_str.split(",") if h.strip())
lr = st.sidebar.slider("Taxa de aprendizado", 0.001, 0.5, 0.05, 0.001)
epochs = st.sidebar.slider("Épocas", 10, 500, 150, 10)
seed = st.sidebar.number_input("Seed", value=42, step=1)
update_every = st.sidebar.slider("Atualizar visualização a cada N épocas", 1, 20, 5)
start = st.sidebar.button("Treinar", type="primary")


# ---------------- Layout do grafo (coordenadas manuais) ----------------
def compute_positions(layer_sizes):
    """Posiciona os nós do grafo manualmente (sem numpy)."""
    positions = []
    n_layers = len(layer_sizes)
    for l, size in enumerate(layer_sizes):
        x = l / (n_layers - 1) if n_layers > 1 else 0.0
        layer_pos = []
        for i in range(size):
            y = 0.5 if size == 1 else i / (size - 1)
            layer_pos.append((x, y))
        positions.append(layer_pos)
    return positions


def build_figure(mlp, positions, max_edges_per_layer=400):
    fig = go.Figure()

    # arestas (linhas), com espessura/cor ~ peso
    for l in range(1, len(mlp.layers)):
        edge_x, edge_y, edge_color = [], [], []
        count = 0
        for node in mlp.layers[l]:
            for e in node.in_edges:
                if count >= max_edges_per_layer:
                    break
                sx, sy = positions[l - 1][e.src.idx]
                dx, dy = positions[l][node.idx]
                edge_x += [sx, dx, None]
                edge_y += [sy, dy, None]
                edge_color.append(e.weight)
                count += 1
        if edge_x:
            fig.add_trace(go.Scatter(
                x=edge_x, y=edge_y, mode='lines',
                line=dict(color='rgba(120,120,120,0.35)', width=1),
                hoverinfo='skip', showlegend=False
            ))

    # nós
    for l, layer_pos in enumerate(positions):
        xs = [p[0] for p in layer_pos]
        ys = [p[1] for p in layer_pos]
        vals = [n.value for n in mlp.layers[l]]
        fig.add_trace(go.Scatter(
            x=xs, y=ys, mode='markers',
            marker=dict(size=14, color=vals, colorscale='Viridis',
                        cmin=0, cmax=1, line=dict(width=1, color='black')),
            hovertext=[f"camada {l} | nó {i} | ativação={v:.3f}"
                       for i, v in enumerate(vals)],
            hoverinfo='text', showlegend=False
        ))

    fig.update_layout(
        height=500, margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(visible=False), yaxis=dict(visible=False),
        plot_bgcolor='white'
    )
    return fig


def accuracy(mlp, X, y):
    correct = sum(1 for xi, yi in zip(X, y) if (mlp.predict(xi) >= 0.5) == bool(yi))
    return correct / len(X)


# ---------------- Área principal ----------------
col_graph, col_metrics = st.columns([2, 1])
graph_placeholder = col_graph.empty()
loss_placeholder = col_metrics.empty()
acc_placeholder = col_metrics.empty()
status_placeholder = col_metrics.empty()

if start:
    X_train, y_train, X_test, y_test, input_size, stats = load_dataset('heart.csv', seed=seed)
    layer_sizes = [input_size, *hidden, 1]
    mlp = MLP(layer_sizes, seed=seed, lr=lr)
    positions = compute_positions(layer_sizes)

    st.sidebar.write(f"Arquitetura: {layer_sizes}")
    st.sidebar.write(f"Treino: {len(X_train)} | Teste: {len(X_test)}")

    rng = random.Random(seed)
    loss_history, train_acc_history, test_acc_history = [], [], []

    for epoch in range(1, epochs + 1):
        order = list(range(len(X_train)))
        rng.shuffle(order)
        total_loss = 0.0
        for i in order:
            _, loss = mlp.train_step(X_train[i], y_train[i])
            total_loss += loss
        avg_loss = total_loss / len(X_train)
        loss_history.append(avg_loss)

        if epoch % update_every == 0 or epoch == epochs:
            tr_acc = accuracy(mlp, X_train, y_train)
            te_acc = accuracy(mlp, X_test, y_test)
            train_acc_history.append(tr_acc)
            test_acc_history.append(te_acc)

            # rede: última ativação do último exemplo usado fica nos nós -> ok p/ visual
            fig = build_figure(mlp, positions)
            graph_placeholder.plotly_chart(fig, use_container_width=True,
                                            key=f"graph_{epoch}")
            loss_placeholder.line_chart({"loss": loss_history})
            acc_placeholder.line_chart({"train_acc": train_acc_history,
                                         "test_acc": test_acc_history})
            status_placeholder.info(
                f"Época {epoch}/{epochs} | loss={avg_loss:.4f} | "
                f"train_acc={tr_acc:.3f} | test_acc={te_acc:.3f}"
            )

    st.success("Treinamento concluído!")

    # ---------------- Inferência interativa ----------------
    st.subheader("Inferência em um caso de teste")
    idx = st.slider("Escolha um exemplo do conjunto de teste", 0, len(X_test) - 1, 0)
    if st.button("Rodar inferência neste exemplo"):
        pred = mlp.predict(X_test[idx])
        fig = build_figure(mlp, positions)
        st.plotly_chart(fig, use_container_width=True, key="inference_graph")
        label_pred = "Doença cardíaca" if pred >= 0.5 else "Sem doença cardíaca"
        label_real = "Doença cardíaca" if y_test[idx] == 1.0 else "Sem doença cardíaca"
        st.write(f"**Predição:** {label_pred} (score={pred:.3f})")
        st.write(f"**Rótulo real:** {label_real}")
else:
    st.info("Configure os hiperparâmetros na barra lateral e clique em **Treinar**.")

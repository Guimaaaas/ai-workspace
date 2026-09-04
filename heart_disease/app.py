import random
import time
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
student_name = st.sidebar.text_input("Seu nome", "")
hidden_str = st.sidebar.text_input("Camadas ocultas (separadas por vírgula)", "16,8")
hidden = tuple(int(h.strip()) for h in hidden_str.split(",") if h.strip())
lr = st.sidebar.slider("Taxa de aprendizado", 0.001, 0.5, 0.05, 0.001)
epochs = st.sidebar.slider("Épocas", 10, 500, 150, 10)
seed = st.sidebar.number_input("Seed", value=42, step=1)
update_every = st.sidebar.slider("Atualizar visualização a cada N épocas", 1, 20, 5)
start = st.sidebar.button("Treinar", type="primary")

PREPROCESSING_DESC = "standardize (z-score nas contínuas) + one-hot nas categóricas + binárias brutas"
ACTIVATION_DESC = "sigmoid"


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


def build_figure(mlp, positions, max_edges_per_layer=400, highlight_layer=None, highlight_mode=None):
    """highlight_mode: 'forward' destaca arestas ENTRANDO em highlight_layer;
       'backward' destaca arestas SAINDO de highlight_layer (rumo à camada anterior)."""
    fig = go.Figure()

    for l in range(1, len(mlp.layers)):
        edge_x, edge_y = [], []
        hi_x, hi_y = [], []
        count = 0
        for node in mlp.layers[l]:
            for e in node.in_edges:
                if count >= max_edges_per_layer:
                    break
                sx, sy = positions[l - 1][e.src.idx]
                dx, dy = positions[l][node.idx]
                is_highlighted = (highlight_mode == 'forward' and l == highlight_layer) or \
                                  (highlight_mode == 'backward' and l == highlight_layer)
                if is_highlighted:
                    hi_x += [sx, dx, None]
                    hi_y += [sy, dy, None]
                else:
                    edge_x += [sx, dx, None]
                    edge_y += [sy, dy, None]
                count += 1
        if edge_x:
            fig.add_trace(go.Scatter(
                x=edge_x, y=edge_y, mode='lines',
                line=dict(color='rgba(120,120,120,0.25)', width=1),
                hoverinfo='skip', showlegend=False
            ))
        if hi_x:
            color = 'rgba(230,60,60,0.85)' if highlight_mode == 'forward' else 'rgba(60,120,230,0.85)'
            fig.add_trace(go.Scatter(
                x=hi_x, y=hi_y, mode='lines',
                line=dict(color=color, width=2.2),
                hoverinfo='skip', showlegend=False
            ))

    for l, layer_pos in enumerate(positions):
        xs = [p[0] for p in layer_pos]
        ys = [p[1] for p in layer_pos]
        vals = [n.value for n in mlp.layers[l]]
        border_width = 3 if l == highlight_layer else 1
        border_color = ('crimson' if highlight_mode == 'forward' else 'royalblue') if l == highlight_layer else 'black'
        fig.add_trace(go.Scatter(
            x=xs, y=ys, mode='markers',
            marker=dict(size=16 if l == highlight_layer else 14, color=vals,
                        colorscale='Viridis', cmin=0, cmax=1,
                        line=dict(width=border_width, color=border_color)),
            hovertext=[f"camada {l} | nó {i} | z={n.z:.3f} | ativação={n.value:.3f} | delta={n.delta:.4f}"
                       for i, n in enumerate(mlp.layers[l])],
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

    # guarda tudo em session_state para sobreviver aos reruns dos botões abaixo
    st.session_state.trained_mlp = mlp
    st.session_state.trained_positions = positions
    st.session_state.trained_data = (X_train, y_train, X_test, y_test)
    st.session_state.trained_layer_sizes = layer_sizes
    st.session_state.trained_lr = lr
    st.session_state.trained_test_acc = test_acc_history[-1]
    st.session_state.trained_student_name = student_name

if 'trained_mlp' in st.session_state:
    mlp = st.session_state.trained_mlp
    positions = st.session_state.trained_positions
    X_train, y_train, X_test, y_test = st.session_state.trained_data
    layer_sizes = st.session_state.trained_layer_sizes

    # ---------------------- Card de resultado final ----------------------
    name_display = st.session_state.trained_student_name or "Aluno(a)"
    st.markdown(f"## {st.session_state.trained_test_acc:.3f} : {name_display}")
    c_acc, c_lr, c_act, c_arch, c_prep = st.columns(5)
    c_acc.metric("accuracy", f"{st.session_state.trained_test_acc:.3f}")
    c_lr.metric("learning rate", f"{st.session_state.trained_lr:g}")
    c_act.metric("activation", ACTIVATION_DESC)
    c_arch.metric("architecture", " | ".join(str(s) for s in layer_sizes))
    c_prep.metric("pre-processing", "standardize")
    st.caption(f"Pré-processamento completo: {PREPROCESSING_DESC}")
    comments = st.text_area(
        "comentários",
        placeholder="Ex.: o uso da padronização (standardize) ajudou a resolver o problema de gradientes explodindo no meu caso.",
        key="result_comments",
    )

    # ---------------------- Passo a passo: Feedforward / Backprop ----------------------
    st.subheader("Passo a passo: Feedforward e Backpropagation")
    st.caption("Escolha um exemplo e veja a informação se propagando pelo grafo, "
               "camada por camada — primeiro para frente (feedforward, vermelho), "
               "depois para trás (backprop, azul).")

    n_layers = len(layer_sizes)
    n_forward_steps = n_layers - 1     # camadas 1..L-1 (transições)
    n_backward_steps = n_layers - 1    # deltas calculados da saída até a entrada
    total_steps = n_forward_steps + n_backward_steps

    if 'step_idx' not in st.session_state:
        st.session_state.step_idx = 0
    if 'step_example' not in st.session_state:
        st.session_state.step_example = 0

    c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
    example_idx = c1.slider("Exemplo do teste", 0, len(X_test) - 1,
                             st.session_state.step_example, key="step_example_slider")
    st.session_state.step_example = example_idx
    autoplay = c2.toggle("Reprodução automática", value=False)
    if c3.button("Próximo passo ⏭️"):
        st.session_state.step_idx = (st.session_state.step_idx + 1) % (total_steps + 1)
    if c4.button("Reiniciar ⏮️"):
        st.session_state.step_idx = 0

    step = st.session_state.step_idx
    x_ex, y_ex = X_test[example_idx], [y_test[example_idx]]

    if step <= n_forward_steps:
        # fase feedforward: computa até a camada `step` (0 = só entrada, ainda nada propagado)
        mlp.forward_partial(x_ex, up_to_layer=step)
        highlight_layer = step if step > 0 else None
        fig_step = build_figure(mlp, positions, highlight_layer=highlight_layer, highlight_mode='forward')
        fase = f"FEEDFORWARD — calculando camada {step} de {n_forward_steps}" if step > 0 else \
               "FEEDFORWARD — valores de entrada carregados"
    else:
        # fase backprop: já com forward completo; calcula deltas da saída até certa camada
        mlp.forward_partial(x_ex, up_to_layer=n_layers - 1)
        bstep = step - n_forward_steps  # 1..n_backward_steps
        down_to = n_layers - 1 - bstep
        mlp.backward_partial(y_ex, down_to_layer=down_to)
        highlight_layer = n_layers - 1 - (bstep - 1)
        fig_step = build_figure(mlp, positions, highlight_layer=highlight_layer, highlight_mode='backward')
        fase = f"BACKPROP — calculando delta da camada {highlight_layer}"

    st.plotly_chart(fig_step, use_container_width=True, key=f"step_graph_{step}")
    st.info(f"Passo {step}/{total_steps} — {fase}")

    if highlight_layer is not None:
        layer_nodes = mlp.layers[highlight_layer]
        st.write(f"**Valores na camada {highlight_layer}:**")
        st.table({
            "nó": list(range(len(layer_nodes))),
            "z (soma ponderada)": [f"{n.z:.4f}" for n in layer_nodes],
            "ativação (sigmoid)": [f"{n.value:.4f}" for n in layer_nodes],
            "delta": [f"{n.delta:.5f}" for n in layer_nodes],
        })

    pred_final = mlp.layers[-1][0].value
    st.caption(f"Predição da rede para este exemplo: **{pred_final:.3f}** "
               f"({'Doença cardíaca' if pred_final >= 0.5 else 'Sem doença cardíaca'}) "
               f"| Rótulo real: {'Doença cardíaca' if y_test[example_idx] == 1.0 else 'Sem doença cardíaca'}")

    if autoplay:
        time.sleep(1.0)
        st.session_state.step_idx = (st.session_state.step_idx + 1) % (total_steps + 1)
        st.rerun()

    # ---------------- Inferência interativa (predição final, já treinada) ----------------
    st.subheader("Inferência em um caso de teste")
    idx = st.slider("Escolha um exemplo do conjunto de teste", 0, len(X_test) - 1, 0, key="infer_slider")
    if st.button("Rodar inferência neste exemplo"):
        pred = mlp.predict(X_test[idx])
        fig = build_figure(mlp, positions)
        st.plotly_chart(fig, use_container_width=True, key="inference_graph")
        label_pred = "Doença cardíaca" if pred >= 0.5 else "Sem doença cardíaca"
        label_real = "Doença cardíaca" if y_test[idx] == 1.0 else "Sem doença cardíaca"
        st.write(f"**Predição:** {label_pred} (score={pred:.3f})")
        st.write(f"**Rótulo real:** {label_real}")
elif not start:
    st.info("Configure os hiperparâmetros na barra lateral e clique em **Treinar**.")

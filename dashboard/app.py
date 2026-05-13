import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from bulldozer_engine import Bulldozer
from paradox_generators import LogicalAntinomyGenerator
from metrics import GeniusScore

st.set_page_config(page_title="GRA Bulldozer Dashboard", layout="wide")
st.title("GRA-Bulldozer: Interactive Paradox Zeroing")

# Define a test landscape
def test_landscape(x):
    x1, x2 = x[0], x[1]
    return (x1**2 - 1)**2 + x2**2 + 0.3*np.sin(5*x1)

col1, col2 = st.columns(2)
with col1:
    st.header("Landscape before attack")
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-1.5, 1.5, 80)
    X, Y = np.meshgrid(x, y)
    Z = np.array([test_landscape([xx, yy]) for xx, yy in zip(X.flatten(), Y.flatten())]).reshape(X.shape)
    fig1 = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='viridis')])
    fig1.update_layout(title="J(Psi) - Initial Landscape", scene=dict(zaxis_title="Foam"))
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.header("Bulldozer control")
    start_x = st.slider("Start X0", -2.0, 2.0, 1.5)
    start_y = st.slider("Start Y0", -1.5, 1.5, 0.0)
    cycles = st.slider("Max cycles", 1, 20, 5)
    if st.button("Run Bulldozer"):
        gen = LogicalAntinomyGenerator(dim=2, eps=0.1)
        bulldozer = Bulldozer(test_landscape, dim=2, generator=gen,
                              eta=0.01, alpha=0.05)
        start = np.array([start_x, start_y])
        final = bulldozer.run(start, max_cycles=cycles, verbose=False)

        st.success(f"Final state: [{final[0]:.3f}, {final[1]:.3f}], J = {test_landscape(final):.4f}")

        # Show trajectory on contour (simplified: just final point)
        fig2 = px.imshow(Z, x=x, y=y, origin='lower', aspect='auto',
                         labels=dict(x="x1", y="x2", color="J"),
                         title="Final point")
        fig2.add_scatter(x=[final[0]], y=[final[1]], mode='markers',
                         marker=dict(size=12, color='red'), name='bulldozer')
        st.plotly_chart(fig2, use_container_width=True)

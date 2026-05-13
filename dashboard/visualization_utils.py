# Visualization utilities for the GRA Bulldozer dashboard
import numpy as np
import plotly.graph_objects as go

def create_surface_plot(X, Y, Z, title="Landscape", colorscale='viridis'):
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale=colorscale)])
    fig.update_layout(title=title, scene=dict(zaxis_title="J(Psi)"))
    return fig

def create_contour_plot(X, Y, Z, title="Contour Map"):
    fig = go.Figure(data=[go.Contour(z=Z, x=X[0], y=Y[:,0], colorscale='viridis')])
    fig.update_layout(title=title, xaxis_title="x1", yaxis_title="x2")
    return fig

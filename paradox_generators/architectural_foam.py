import numpy as np
from .base import ParadoxGenerator

class ArchitecturalFoamGenerator(ParadoxGenerator):
    """
    Generates a 'foamy' direction using a high-frequency sinusoidal pattern
    that is orthogonal to the gradient.
    """

    def __init__(self, dim: int, eps: float = 0.1, frequency: float = 5.0):
        super().__init__(dim, eps)
        self.frequency = frequency

    def generate(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        # Create a sine wave along each coordinate with random phases
        rng = np.random.default_rng()
        phases = rng.uniform(0, 2*np.pi, size=self.dim)
        v = np.sin(self.frequency * state + phases)
        # Orthogonalize to gradient
        if np.linalg.norm(gradient) > 1e-8:
            v = v - (v @ gradient) / (gradient @ gradient) * gradient
        if np.linalg.norm(v) > 0:
            v = v / np.linalg.norm(v)
        return v

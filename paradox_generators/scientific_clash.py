import numpy as np
from .base import ParadoxGenerator

class ScientificClashGenerator(ParadoxGenerator):
    """
    Simulates a clash between two 'theories' represented by two random orthogonal
    directions. Produces a vector that points from one theory's preferred state to the other.
    """

    def __init__(self, dim: int, eps: float = 0.1, clash_strength: float = 1.0):
        super().__init__(dim, eps)
        self.clash_strength = clash_strength
        # Two random orthonormal bases (theories)
        rng = np.random.default_rng()
        self.theory_a = rng.normal(size=dim)
        self.theory_a = self.theory_a / np.linalg.norm(self.theory_a)
        self.theory_b = rng.normal(size=dim)
        self.theory_b = self.theory_b - (self.theory_b @ self.theory_a) * self.theory_a
        self.theory_b = self.theory_b / np.linalg.norm(self.theory_b) if np.linalg.norm(self.theory_b) > 0 else self.theory_a

    def generate(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        # Direction from theory_a to theory_b
        v = self.theory_b - self.theory_a
        # Orthogonalize to gradient
        if np.linalg.norm(gradient) > 1e-8:
            v = v - (v @ gradient) / (gradient @ gradient) * gradient
        if np.linalg.norm(v) > 0:
            v = v / np.linalg.norm(v)
        return self.clash_strength * v

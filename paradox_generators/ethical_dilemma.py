import numpy as np
from .base import ParadoxGenerator

class EthicalDilemmaGenerator(ParadoxGenerator):
    """
    Generates a paradox by pulling the state towards a 'utilitarian' direction
    and simultaneously towards a 'deontological' direction, then taking the difference.
    """

    def __init__(self, dim: int, eps: float = 0.1, dilemma_factor: float = 1.0):
        super().__init__(dim, eps)
        self.dilemma_factor = dilemma_factor
        rng = np.random.default_rng()
        self.utilitarian = rng.normal(size=dim)
        self.utilitarian = self.utilitarian / np.linalg.norm(self.utilitarian)
        self.deontological = rng.normal(size=dim)
        self.deontological = self.deontological - (self.deontological @ self.utilitarian) * self.utilitarian
        self.deontological = self.deontological / np.linalg.norm(self.deontological) if np.linalg.norm(self.deontological) > 0 else self.utilitarian

    def generate(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        # Conflict: direction from utilitarian to deontological
        v = self.deontological - self.utilitarian
        if np.linalg.norm(gradient) > 1e-8:
            v = v - (v @ gradient) / (gradient @ gradient) * gradient
        if np.linalg.norm(v) > 0:
            v = v / np.linalg.norm(v)
        return self.dilemma_factor * v

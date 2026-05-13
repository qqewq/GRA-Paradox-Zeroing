import numpy as np
from abc import ABC, abstractmethod

class ParadoxGenerator(ABC):
    """Base class for all paradox generators."""

    def __init__(self, dim: int, eps: float = 0.1):
        self.dim = dim
        self.eps = eps

    @abstractmethod
    def generate(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        """
        Generate a paradox vector v_theta(state) that is orthogonal to gradient.

        Args:
            state: current point in H (numpy array shape (dim,))
            gradient: grad J(state) (same shape)

        Returns:
            v_theta: paradox direction (same shape), approximately orthogonal to gradient.
        """
        pass

    def apply(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        """Return Gamma_theta(state) = state + eps * v_theta."""
        v = self.generate(state, gradient)
        return state + self.eps * v

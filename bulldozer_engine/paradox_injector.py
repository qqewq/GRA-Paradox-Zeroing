import numpy as np
from paradox_generators import ParadoxGenerator

class ParadoxInjector:
    """Applies Gamma_theta operator using a given paradox generator."""

    def __init__(self, generator: ParadoxGenerator):
        self.generator = generator

    def inject(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        """Return Psi_paradox = state + eps * v_theta."""
        return self.generator.apply(state, gradient)

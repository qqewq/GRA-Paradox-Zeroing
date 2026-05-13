import numpy as np
from .base import ParadoxGenerator

class LogicalAntinomyGenerator(ParadoxGenerator):
    """
    Generates a vector that flips signs in a random subspace,
    then projects to be orthogonal to the gradient.
    """

    def generate(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        # Random orthogonal direction (Gram-Schmidt on random vectors)
        rng = np.random.default_rng()
        v = rng.normal(size=self.dim)
        # Remove component along gradient
        if np.linalg.norm(gradient) > 1e-8:
            v = v - (v @ gradient) / (gradient @ gradient) * gradient
        # Normalize
        if np.linalg.norm(v) > 0:
            v = v / np.linalg.norm(v)
        return v

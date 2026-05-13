import numpy as np
from scipy.optimize import minimize

class TrenchDetector:
    """
    Finds local minima (trenches) of a given landscape J.
    Uses multiple random restarts.
    """

    def __init__(self, landscape_func, dim: int, n_restarts: int = 10):
        self.J = landscape_func
        self.dim = dim
        self.n_restarts = n_restarts

    def detect(self) -> list:
        """Return list of detected minima (numpy arrays)."""
        minima = []
        for _ in range(self.n_restarts):
            x0 = np.random.uniform(-5, 5, size=self.dim)
            res = minimize(self.J, x0, method='BFGS')
            if res.success:
                # Add if not near existing minima (tolerance 1e-4)
                duplicate = False
                for m in minima:
                    if np.linalg.norm(res.x - m) < 1e-4:
                        duplicate = True
                        break
                if not duplicate:
                    minima.append(res.x)
        return minima

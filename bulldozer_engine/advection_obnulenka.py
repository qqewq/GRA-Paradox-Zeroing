import numpy as np

class AdvectiveZeroing:
    """
    Performs one step of bulldozer flow: 
    Psi_{t+1} = Psi_t - eta grad J + alpha * advection_term,
    where advection_term pulls state towards known trenches.
    """

    def __init__(self, trenches: list, eta: float = 0.01, alpha: float = 0.1, tau: float = 0.5):
        self.trenches = trenches  # list of numpy arrays
        self.eta = eta
        self.alpha = alpha
        self.tau = tau

    def step(self, state: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        gradient_step = -self.eta * gradient

        # Advection term: sum over trenches of (state - mu_k) * sigmoid(J(mu_k))
        advection = np.zeros_like(state)
        for mu in self.trenches:
            # Compute J(mu) is not directly available, we approximate by current state? 
            # Actually we need J at the trench - we assume it's a local minimum so J_small.
            # For simplicity, we use a constant weight 1.0 for all trenches.
            # In full implementation, compute J(mu) by calling landscape.
            weight = 1.0 / (1.0 + np.exp(-self.tau))  # sigmoid-like constant
            advection += self.alpha * weight * (state - mu)

        return state + gradient_step + advection

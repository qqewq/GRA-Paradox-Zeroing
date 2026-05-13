import numpy as np
from .trench_detector import TrenchDetector
from .paradox_injector import ParadoxInjector
from .advection_obnulenka import AdvectiveZeroing

class Bulldozer:
    """
    Combines all components: detect trenches, generate paradox, advectively zero.
    Implements the cycle Gamma_theta -> N.
    """

    def __init__(self, landscape_func, dim: int,
                 generator=None, eta=0.01, alpha=0.1,
                 n_cycles=3, epsilon_paradox=0.05):
        self.J = landscape_func
        self.dim = dim
        self.eta = eta
        self.alpha = alpha
        self.n_cycles = n_cycles
        self.epsilon_paradox = epsilon_paradox

        # Default paradox generator (logical antinomy)
        from paradox_generators import LogicalAntinomyGenerator
        if generator is None:
            generator = LogicalAntinomyGenerator(dim=dim, eps=epsilon_paradox)
        self.injector = ParadoxInjector(generator)

    def run(self, initial_state: np.ndarray, max_cycles: int = 10, verbose: bool = False):
        state = initial_state.copy()

        for cycle in range(max_cycles):
            # 1. Detect trenches (local minima)
            detector = TrenchDetector(self.J, self.dim)
            trenches = detector.detect()
            if verbose:
                print(f"Cycle {cycle+1}: detected {len(trenches)} trenches")

            # 2. Generate paradox state (Gamma_theta)
            grad = self._numerical_gradient(state)
            state_paradox = self.injector.inject(state, grad)

            # 3. Zeroing with advection (N)
            zeroing = AdvectiveZeroing(trenches, eta=self.eta, alpha=self.alpha)
            # We need to re-evaluate gradient at state_paradox
            grad_paradox = self._numerical_gradient(state_paradox)
            state_new = zeroing.step(state_paradox, grad_paradox)

            # Evaluate improvement
            old_value = self.J(state)
            new_value = self.J(state_new)
            if verbose:
                print(f"  J: {old_value:.4f} -> {new_value:.4f}")

            state = state_new

            # Early stopping if near global vacuum (tunable threshold)
            if new_value < 1e-6:
                break

        return state

    def _numerical_gradient(self, x, eps=1e-6):
        grad = np.zeros_like(x)
        for i in range(self.dim):
            x_plus = x.copy()
            x_minus = x.copy()
            x_plus[i] += eps
            x_minus[i] -= eps
            grad[i] = (self.J(x_plus) - self.J(x_minus)) / (2*eps)
        return grad

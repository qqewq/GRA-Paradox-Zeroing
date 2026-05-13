import numpy as np

class GeniusScore:
    """
    Evaluates how 'genius' a given paradox injection was:
    - Reduction in global minimum after cycle
    - Number of new transitions opened
    - Smoothness of the post-attack landscape
    """

    def __init__(self, landscape_func):
        self.J = landscape_func

    def compute(self, state_before, state_after, trenches_before, trenches_after) -> float:
        # Reduction in J at the state
        delta_J = self.J(state_before) - self.J(state_after)
        # Increase in number of accessible trenches (simplified: count difference)
        delta_trenches = len(trenches_after) - len(trenches_before)
        # Combine into score (higher is better)
        score = delta_J + 0.1 * delta_trenches
        return max(0, score)

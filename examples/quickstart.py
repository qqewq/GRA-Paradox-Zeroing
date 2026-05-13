from paradox_generators import LogicalAntinomyGenerator
from bulldozer_engine import Bulldozer
import numpy as np

def landscape(x):
    return (x[0]**2 - 1)**2 + x[1]**2 + 0.5*np.sin(5*x[0])

bulldozer = Bulldozer(landscape, dim=2)
final_state = bulldozer.run(initial_state=np.array([2.0, 0.5]),
                           max_cycles=5,
                           verbose=True)
print(f"Global minimum: {final_state}, Phi = {landscape(final_state):.4f}")

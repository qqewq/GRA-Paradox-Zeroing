# Generates ethical paradoxes and zeroes them into Alania laws.
import numpy as np
from bulldozer_engine import Bulldozer
from paradox_generators import EthicalDilemmaGenerator

def alania_landscape(x):
    # x[0]: 'harm' axis, x[1]: 'care' axis, x[2]: 'zeroing_power'
    # Ideal: zero harm, high care, moderate zeroing power
    return (x[0]**2) + (1 - x[1])**2 + (0.5 - x[2])**2 + 0.5*np.sin(5*x[0])*np.cos(5*x[1])

if __name__ == "__main__":
    generator = EthicalDilemmaGenerator(dim=3, eps=0.1, dilemma_factor=1.2)
    bulldozer = Bulldozer(alania_landscape, dim=3, generator=generator,
                          eta=0.02, alpha=0.1)
    start = np.array([1.0, 0.0, 1.0])  # high harm, low care, high power
    final = bulldozer.run(start, max_cycles=12, verbose=True)
    print("\nAlania Constitution point (harm~0, care~1, zeroing~0.5):")
    print(final)
    print(f"J = {alania_landscape(final):.4f}")

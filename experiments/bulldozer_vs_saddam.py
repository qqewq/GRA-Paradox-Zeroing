import numpy as np
import matplotlib.pyplot as plt
from bulldozer_engine import Bulldozer
from paradox_generators import ScientificClashGenerator

# "Saddam function" - two minima, one deeper but separated by high barrier
def saddam_landscape(x):
    # x is 2D array
    x1, x2 = x[0], x[1]
    # Two wells: shallow at (1,0), deep at (-1,0)
    shallow = (x1 - 1)**2 + x2**2
    deep = (x1 + 1)**2 + x2**2
    # Barrier: high ridge at x1=0
    barrier = 5 * np.exp(-x1**2 / 0.1)
    return shallow + deep + barrier - 2.0  # adjusted so deep is ~0

if __name__ == "__main__":
    # Use scientific clash generator for this experiment
    generator = ScientificClashGenerator(dim=2, eps=0.2, clash_strength=1.5)
    bulldozer = Bulldozer(saddam_landscape, dim=2, generator=generator,
                          eta=0.01, alpha=0.15, n_cycles=5)

    start = np.array([2.0, 0.0])
    final = bulldozer.run(start, max_cycles=10, verbose=True)

    print(f"\nGlobal deep minimum ~ (-1,0) with J ~ {saddam_landscape(np.array([-1.0,0.0])):.4f}")
    print(f"Bulldozer found: {final}, J = {saddam_landscape(final):.4f}")

    # Quick contour plot
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-1, 1, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.array([saddam_landscape([xx, yy]) for xx, yy in zip(X.flatten(), Y.flatten())]).reshape(X.shape)

    plt.figure(figsize=(8,6))
    plt.contourf(X, Y, Z, levels=30)
    plt.plot(start[0], start[1], 'ro', label='start')
    plt.plot(final[0], final[1], 'g*', markersize=12, label='bulldozer final')
    plt.plot(-1, 0, 'b+', markersize=10, label='true global min')
    plt.legend()
    plt.title("Bulldozer vs Saddam function: escapes shallow minimum")
    plt.savefig("bulldozer_vs_saddam.png")
    plt.show()

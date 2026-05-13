import numpy as np

def random_orthonormal_basis(dim: int, gradient: np.ndarray = None) -> list:
    """Create an orthonormal basis where the first vector is gradient (if provided)."""
    rng = np.random.default_rng()
    basis = []
    if gradient is not None and np.linalg.norm(gradient) > 0:
        u1 = gradient / np.linalg.norm(gradient)
        basis.append(u1)
    else:
        u1 = rng.normal(size=dim)
        u1 = u1 / np.linalg.norm(u1)
        basis.append(u1)

    # Gram-Schmidt for remaining dim-1 vectors
    for _ in range(dim-1):
        v = rng.normal(size=dim)
        for u in basis:
            v = v - (v @ u) * u
        if np.linalg.norm(v) > 1e-8:
            v = v / np.linalg.norm(v)
        else:
            v = np.zeros(dim)
            v[_ % dim] = 1.0
            for u in basis:
                v = v - (v @ u) * u
            v = v / np.linalg.norm(v)
        basis.append(v)
    return basis

import numpy as np
from paradox_generators import LogicalAntinomyGenerator, ScientificClashGenerator

def test_orthogonality():
    gen = LogicalAntinomyGenerator(dim=3, eps=0.1)
    state = np.array([1.0, 0.0, 0.0])
    grad = np.array([2.0, 1.0, 0.0])
    v = gen.generate(state, grad)
    assert abs(np.dot(v, grad)) < 1e-7, "Not orthogonal to gradient"

def test_scientific_clash_shape():
    gen = ScientificClashGenerator(dim=4)
    state = np.zeros(4)
    grad = np.ones(4)
    v = gen.generate(state, grad)
    assert v.shape == (4,)

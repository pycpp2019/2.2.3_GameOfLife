import pytest

import numpy as np

from life import step


def test_oscillator():
    data = np.array([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ], dtype=np.bool)

    new_data = step(data)
    ref_data = np.array([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
    ], dtype=np.bool)

    assert np.all(new_data == ref_data)

def test_glider():
    data = np.array([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ], dtype=np.bool)

    new_data = data
    for _ in range(20):
        new_data = step(new_data)

    assert np.all(data == new_data)

@pytest.mark.timeout(60)
def test_glider_large_field():
    size = 400
    data = np.zeros((size, size), dtype=np.bool)
    data[:5,:5] = np.array([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ], dtype=np.bool)

    new_data = data
    for _ in range(4*size):
        new_data = step(new_data)

    assert np.all(data == new_data)

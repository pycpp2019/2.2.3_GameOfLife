import numpy as np

from life import step

def test_glider():
    data = np.array([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ], dtype=np.bool)

    new_data = data
    for _ in range(2*10):
        new_data = step(new_data)

    assert np.all(data == new_data)

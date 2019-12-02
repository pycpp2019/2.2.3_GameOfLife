import numpy as np

def step(state):
    adj = np.zeros(state.shape)
    for j in range(-1, 2):
        for i in range(-1, 2):
            if i != 0 or j != 0:
                adj += np.roll(state, (j, i), axis=(1, 0))
    eq2 = adj == 2
    eq3 = adj == 3
    return np.logical_or(
        np.logical_and(state, np.logical_or(eq2, eq3)), # not die
        np.logical_and(np.logical_not(state), eq3) # born
    )

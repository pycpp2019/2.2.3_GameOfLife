import numpy as np

def step(state):
    
    state_int = state.astype(int)
    tmp_state = (np.roll(state_int, 1, axis = 0)
        + np.roll(np.roll(state_int, 1, axis = 0), 1, axis = 1)
        + np.roll(np.roll(state, 1, axis = 0), -1, axis = 1)
        + np.roll(state, -1, axis = 0)
        + np.roll(np.roll(state, -1, axis = 0), 1, axis = 1)
        + np.roll(np.roll(state, -1, axis = 0), -1, axis = 1)
        + np.roll(state, 1, axis = 1)
        + np.roll(state, -1, axis = 1)
        )

    return state * np.logical_or(tmp_state == 2, tmp_state == 3) + (tmp_state == 3)
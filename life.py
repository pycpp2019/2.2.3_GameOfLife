import numpy as np

def step(state):
    new_state = -np.array(state, dtype=int)
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            new_state += np.roll(np.roll(state, i, axis=0), j, axis=1)
    return np.logical_or(new_state==3, np.logical_and(new_state==2, state==True))
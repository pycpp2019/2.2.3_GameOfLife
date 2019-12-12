import numpy as np

def step(state):
    state2=state*1
    S=np.roll(state2, 1, axis=0)+np.roll(state2, -1, axis=0)+np.roll(state2, 1, axis=1)+np.roll(state2, -1, axis=1)+np.roll(np.roll(state2, 1, axis=0), 1, axis=1)+np.roll(np.roll(state2,-1,axis=0), 1, axis=1)+np.roll(np.roll(state2, 1, axis=0), -1, axis=1)+np.roll(np.roll(state2, -1, axis=0), -1, axis=1)
    return np.logical_or((S==3),(((S==2)*state)))
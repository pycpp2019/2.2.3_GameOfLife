import numpy as np
import matplotlib.pyplot as plt
'''
def step(state):
    def get_neighbours (x, y):
    return np.sum(state[(x-1):(x+2),(y-1):(y+2)])-state[x,y]
    for index, value in np.ndenumerate(state):
        new_state = state
        num_neighbours = get_neighbours (index[0],index[1])
        if state[index[0], index[1]] and not (2 <= num_neighbours <= 3):
            new_state[index[0], index[1]] = 0
        elif num_neighbours == 3:
            new_state[index[0], index[1]] = 1
    return(new_state)
import numpy as np
'''
def step(state):
    state_new=np.array(state,dtype=int)
    Sum=np.roll(state_new, 1, axis=0)+np.roll(state_new, -1, axis=0)+np.roll(state_new, 1, axis=1)+np.roll(state_new, -1, axis=1)+np.roll(np.roll(state_new, 1, axis=0), 1, axis=1)+np.roll(np.roll(state_new,-1,axis=0), 1, axis=1)+np.roll(np.roll(state_new, 1, axis=0), -1, axis=1)+np.roll(np.roll(state_new, -1, axis=0), -1, axis=1)
    return np.logical_or((Sum==3),(((Sum==2)*state)))

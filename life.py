import numpy as np

def step(state):
    return  (neighbors(state)==3)  +  ( state * (neighbors(state)==2)  ) 

def ver():
    return 2
        
def neighbors(state):
    st=1*state
    return (np.roll(st, 1, axis = 0) + 
            np.roll(st,-1, axis = 0) +
            np.roll(st, 1, axis = 1) +
            np.roll(st,-1, axis = 1) +
            np.roll(np.roll(st, 1, axis = 1), 1, axis = 0) +
            np.roll(np.roll(st,-1, axis = 1), 1, axis = 0) +
            np.roll(np.roll(st, 1, axis = 1),-1, axis = 0) +
            np.roll(np.roll(st,-1, axis = 1),-1, axis = 0))

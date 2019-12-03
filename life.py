import numpy as np
def step(state):
	state1=np.array(state,dtype=int)
	StateSum=np.roll(state1,1,axis=0)+np.roll(state1,-1,axis=0)+np.roll(state1,1,axis=1)+np.roll(state1,-1,axis=1)+np.roll(np.roll(state1,1,axis=0),1,axis=1)+np.roll(np.roll(state1,1,axis=0),-1,axis=1)+np.roll(np.roll(state1,-1,axis=0),1,axis=1)+np.roll(np.roll(state1,-1,axis=0),-1,axis=1)
	return state*np.logical_or(StateSum == 2, StateSum == 3)+(StateSum == 3)

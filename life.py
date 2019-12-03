import numpy as np
def step(state):
	state=np.array(state)
	StateSum=np.roll(state,1,axis=0)+np.roll(state,-1,axis=0)+np.roll(state,1,axis=1)+np.roll(state,-1,axis=1)+np.roll(np.roll(state,1,axis=0),1,axis=1)+np.roll(np.roll(state,1,axis=0),-1,axis=1)+np.roll(np.roll(state,-1,axis=0),1,axis=1)+np.roll(np.roll(state,-1,axis=0),-1,axis=1)
	StateSum2 = StateSum == 2
	StateSum3 = StateSum == 3
	StateSum = np.logical_or(np.logical_and(StateSum2 ,state),StateSum3)
	return StateSum

import numpy as np
	
def TwoAndThree(a):
	if a==2 or a==3:
		return 1
	else:
		return 0

def Three(a):
	if a==3:
		return 1
	else:
		return 0

def step(state):
	state=np.array(state)
	stateSum=np.roll(state,1,axis=0)+np.roll(state,-1,axis=0)+np.roll(state,1,axis=1)+np.roll(state,-1,axis=1)+np.roll(np.roll(state,1,axis=0),1,axis=1)+np.roll(np.roll(state,1,axis=0),-1,axis=1)+np.roll(np.roll(state,-1,axis=0),1,axis=1)+np.roll(np.roll(state,-1,axis=0),-1,axis=1)
	TwoAndThreeV=np.vectorize(TwoAndThree)
	ThreeV=np.vectorize(Three)
	StateSumTT=TwoAndThreeV(stateSum)*state
	StateSumT=np.logical_xor(ThreeV(stateSum),state)*ThreeV(stateSum)
	return np.array(StateSumT+StateSumTT,dtype=bool)
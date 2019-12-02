import numpy as np
	
def BornOrDie(a,b):
	if a==0 and b==3:
		return 1
	if a==1 and (b<2 or b>3):
		return 0
	return a

def step(state):
	state=np.array(state)
	stateSum=np.roll(state,1,axis=0)+np.roll(state,-1,axis=0)+np.roll(state,1,axis=1)+np.roll(state,-1,axis=1)+np.roll(np.roll(state,1,axis=0),1,axis=1)+np.roll(np.roll(state,1,axis=0),-1,axis=1)+np.roll(np.roll(state,-1,axis=0),1,axis=1)+np.roll(np.roll(state,-1,axis=0),-1,axis=1)
	VBornOrDie=np.vectorize(BornOrDie)
	return VBornOrDie(state,stateSum)



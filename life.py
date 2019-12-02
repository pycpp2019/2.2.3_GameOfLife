import numpy as np

def step(state):
    shape = np.shape(state)
    new_state =np.zeros((shape[0]+2,shape[1]+2))
    
    new_state[:-2,:-2] += state
    new_state[1:-1,:-2] += state
    new_state[2:,:-2] += state
    new_state[2:,1:-1] += state
    new_state[2:,2:] += state
    new_state[1:-1,2:] += state
    new_state[:-2,2:] += state
    new_state[:-2,1:-1:] += state
    
    new_state[1,1:-1] += new_state[-1,1:-1]
    new_state[-2,1:-1] += new_state[0,1:-1]
    new_state[1:-1,1] += new_state[1:-1,-1]
    new_state[1:-1,-2] += new_state[1:-1,0]
    new_state[-2,-2] += new_state[0,0]
    new_state[1,1] += new_state[-1,-1]
    new_state[-2,1] += new_state[0,-1]
    new_state[1,-2] += new_state[-1,0]
    
    
    new_state = new_state[1:-1,1:-1]
    new_state = state*(new_state-0)*(new_state-1)*(new_state-4)*(new_state-5)*(new_state-6)*(new_state-7)*(new_state-8)+(new_state-0)*(new_state-1)*(new_state-2)*(new_state-4)*(new_state-5)*(new_state-6)*(new_state-7)*(new_state-8)
    new_state = new_state.astype("bool")
    return new_state
    

'''a = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0],],dtype=np.bool)
for i in range(15):
    print(a)
    a = step(a)'''

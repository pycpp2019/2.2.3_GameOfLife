import numpy as np

def step(state):
    shape = np.shape(state)
    new_state =np.zeros((shape[0]+2,shape[1]+2))
    bool_new_state = np.zeros(shape,dtype =np.bool)
    
    new_state[:-2,:-2] += state
    new_state[1:-1,:-2] += state
    new_state[2:,:-2] += state
    new_state[2:,1:-1] += state
    new_state[2:,2:] += state
    new_state[1:-1,2:] += state
    new_state[:-2,2:] += state
    new_state[:-2,1:-1:] += state
    new_state = new_state[1:-1,1:-1]
    new_state = state*(new_state-0)*(new_state-1)*(new_state-4)*(new_state-5)*(new_state-6)*(new_state-7)*(new_state-8)+(new_state-0)*(new_state-1)*(new_state-2)*(new_state-4)*(new_state-5)*(new_state-6)*(new_state-7)*(new_state-8)
    for i in range(shape[0]):
        for j in range(shape[1]):
            bool_new_state[i,j] = np.bool(new_state[i,j])
    return bool_new_state
    

'''a = np.array([[False,True,False],[False,True,False],[False,True,False],[False,False,False]])
print(step(a))
print(step(step(a)))
print(step(step(step(a))))
print(a)'''
import numpy as np

def step(state):
    width = state[0].size
    hight = state.size // width

    next_step = np.array(state)

    for row_ind in np.arange(hight):
    	for col_ind in np.arange(width):
    		statement = state[row_ind][col_ind]
    		neighbours = sum([state[i % hight][j % width] for i in range(row_ind - 1, row_ind + 2) for j in range(col_ind - 1, col_ind + 2)]) - statement
    		if(neighbours == 3):
    			next_step[row_ind][col_ind] = True
    		elif(neighbours != 2 and neighbours != 3):
    			next_step[row_ind][col_ind] = False

    return next_step

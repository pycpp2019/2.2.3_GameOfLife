import numpy as np
	

def step(state):
	state=np.array(state)
	stateNew=np.array(state)
	for i in range(len(state)):
		for j in range(len(state[0])):
			s=0
			if(i!=0 and j!=0):
				s+=state[i-1][j-1]
			else:
				if(i==0 and j!=0):
					s+=state[len(state)-1][j-1]
				if(i!= 0 and j==0):
					s+=state[i-1][len(state[0])-1]
				if(i==0 and j==0):
					s+= state[len(state)-1][len(state[0])-1]

			
			if(i!=0):
				s+=state[i-1][j]
			else:
				s+=state[len(state)-1][j]


			if(i!=0 and j!=len(state[0])-1):
				s+=state[i-1][j+1]
			else:
				if(i==0 and j!=len(state[0])-1):
					s+= state[len(state)-1][j+1]
				if(i==0 and j==len(state[0])-1):
					s+= state[len(state)-1][0]
				if(i!=0 and j==len(state[0])-1):
					s+= state[i-1][0]
			
			if(j!=len(state[0])-1):
				s+=state[i][j+1]
			else:
				s+=state[i][0]

			if(i!=len(state)-1 and j!=len(state[0])-1):
				s+=state[i+1][j+1]
			else:
				if(i==len(state)-1 and j!=len(state[0])-1):
					s+= state[0][j+1]
				if(i==len(state)-1 and j==len(state[0])-1):
					s+= state[0][0]
				if(i!=len(state)-1 and j==len(state[0])-1):
					s+= state[i+1][0]

			
			if i!=len(state)-1:
				s+=state[i+1][j]
			else:
				s+=state[0][j]

			if i!=len(state)-1 and j!=0:
				s+=state[i+1][j-1]
			else:
				if i==len(state)-1 and j!=0:
					s+= state[0][j-1]
				if i==len(state)-1 and j==len(state[0])-1:
					s+= state[0][len(state[0])-1]
				if i!=len(state)-1 and j==len(state[0])-1:
					s+= state[i+1][len(state[0]-1)]

			if(j!=0):
				s+=state[i][j-1]
			else:
				s+=state[i][len(state[0])-1]
			if(state[i][j]==1 and (s<2 or s>3)):
				stateNew[i][j]=0
			if(state[i][j]==0 and s==3):
				stateNew[i][j]=1

	return stateNew
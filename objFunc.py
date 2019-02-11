import numpy as np 
sqrt2 = 1/np.sqrt(2)
h1 = np.array([0.5,0.5,0])
y = np.array([1,1.5,2])
input = np.array([[0,0,0],[0,1,0],[1,0,0],[1,1,0]])
output = np.array([0,1,1,0])
for i in range(len(input)):
    h = np.dot(input[i],h1)
    input2 = np.copy(input[i])
    input2[2] = h
    z = np.dot(input2,y)
    print z

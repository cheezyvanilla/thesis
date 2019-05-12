
import numpy as np
from qbitgen import qbit

# x = np.array([[0,0,1,0],[0,1,1,0],[1,0,1,0],[1,1,1,0]])
# y = np.array([0,1,1,0])
# netHid = np.array([ -2, -2, 1.7,0]).astype(float)
# netOut = np.array([2.6, 2.6, -2.7, 5.3]).astype(float)
# net = np.array([netHid, netOut])

qbit = qbit()

x = np.array([[1,1],[1,0],[0,1],[0,0]])
y= np.array([1,1,1,0])
input = 2
hidden = 3
output = 1
net = np.zeros((input+hidden+output,input+hidden+output))
for i in range(input+hidden+output): 
    for j in  range(input+hidden+output):
        for hid in range(hidden):
            if i>(input-1)+hid and j <input+hid:
                net[i][j] = 1/np.sqrt(2)

        if i>(input+hidden-1) and j<(input+hidden):
            net[i][j] = 1/np.sqrt(2)
realNet = np.copy(net)
qbit.convert(net, realNet)
print realNet


# for i in (x):
#     i = np.append(i,np.zeros(np.shape(net)[1]-np.shape(x)[1]))    #menyamakan dimensi input dan beban
#     # hidden Fz
#     for j in range(hidden):
#         i[input+j] =  1/(1+np.exp(-np.dot(net[input+ j], i)))

#         print i,1/(1+np.exp(-np.dot(net[input+ j], i)))
#     for k in range(output):
#         print 1/(1+np.exp(-np.dot(net[input+hidden+k], i)))
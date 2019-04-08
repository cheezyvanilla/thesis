from qbitgen import qbit
import numpy as np
qbit  = qbit()
generation = 1
class individual:
    def __init__(self, Qc, k):
        self.Qc = Qc
        self.Qw = np.zeros((np.shape(self.Qc)[0],np.shape(self.Qc)[1], 5))
        self.Qw.fill(sqrt2)
        self.RQc = np.copy(self.Qc)
        self.RQw = np.copy(self.Qw)
        self.Rw = np.copy(self.Qc)
        self.k = k
        width = (float(self.k)/2**self.k)
        edge = -(width*(2**self.k-1)/2)
        a = np.array([i for i in range(2**self.k)])
        b = np.array([edge+(width*i) for i in range(2**self.k)])
        self.z = dict(zip(a,b))
Qc = np.zeros((1,2,3))
sqrt2 = 1/np.sqrt(2)
Qc = np.array([[sqrt2, sqrt2,0],[sqrt2, sqrt2, sqrt2]])     #Qc init
# obj = individual(Qc)
subp3 = [0 for i in range(30)]
subp2 = [0 for i in range(30)]
subp1 = [0 for i in range(30)]

populasi = [subp1, subp2, subp3]
for i in range(len(populasi)):              #INIT INDIVIDUAL OBJECTS
    for j in range(len(populasi[i])):
        populasi[i][j]= individual(Qc,5)

#MAIN LOOP        
for i in range(generation):
    for j in range(len(populasi)):
        for k in range(len(populasi[j])):
            qbit.convert(populasi[j][k].Qc, populasi[j][k].RQc)     #Qc OBSERVATION
            qbit.weightSpaceDef(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].RQw, populasi[j][k].Rw,populasi[j][k].z)
# print (populasi[0][0].RQw[0][0][0])

# print populasi[0][0].RQw
       

# for k in range(len(populasi[0])):
#     qbit.convert(populasi[0][k].Qc, populasi[0][k].RQc)
#     print populasi[0][k].RQc





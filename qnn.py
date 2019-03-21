from qbitgen import qbit
import numpy as np
class individual:
    def __init__(self, Qc):
        self.Qc = Qc
        self.Qw = np.zeros((np.shape(self.Qc)[0],np.shape(self.Qc)[1], 5))
        self.Qw.fill(sqrt2)
        self.RQc = np.copy(self.Qc)
Qc = np.zeros((1,2,3))
sqrt2 = 1/np.sqrt(2)
Qc = np.array([[sqrt2, sqrt2,0],[sqrt2, sqrt2, sqrt2]])     #Qc init
obj = individual(Qc)
subp3 = [0 for i in range(30)]
subp2 = [0 for i in range(30)]
subp1 = [0 for i in range(30)]

populasi = [subp1, subp2, subp3]
for i in range(len(populasi)):              #INIT INDIVIDUAL OBJECTS
    for j in range(len(populasi[i])):
        populasi[i][j]= individual(Qc)






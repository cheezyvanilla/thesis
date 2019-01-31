
import numpy as np
class qbit():
    def __init__(self):
       return None
    def convert(self, qbit, bin ):                 #real connection value encoding
        r = np.random.sample(len(qbit))
        # print r
        for i in range(len(qbit)):
            if r[i] < qbit[i]**2:
                bin[i]= 1
            else:
                bin[i]= 0
        return 0
    def weightspace(self,realconvalue, qbit, bin):
        for i in range (len(realconvalue)):
            if realconvalue[i] == 1:
                 self.convert(qbit[i], bin[i])
    def realWeightValues(self,RQc, RQw,binbit, Rw): #binbit =binarybit, Rw = real weight values
         for i in range (len(RQc)):
            if RQc[i] == 1:
                binbit[i]= {'[ 0.  0.]':np.array([-0.75,0.05]), '[ 0.  1.]':np.array([-0.25,0.05]), '[ 1.  0.]':np.array([0.25,0.05]), '[ 1.  1.]':np.array([0.75,0.05])}[str(RQw[i])]
                Rw[i] = np.random.normal(binbit[i][0],binbit[i][1])

Qc = np.zeros((3,3)) #network Qconnection
Qw = np.zeros((3,2)) #network Qweight
Qw[0] = Qw[1] =Qw[2]= np.array([[1/np.sqrt(2), 1/np.sqrt(2)]])
RQw =np.zeros((3,2)) #realbit weight
Qc[0] = np.array([1/np.sqrt(2), 1/np.sqrt(2), 1/np.sqrt(2)])

RQc = np.zeros((3,3)) #real connection
s = np.zeros((3,3))

subspace = np.zeros((3,2)) #binarybit of subspace values
Rw = np.zeros((1,3))
#main
ilopyu = qbit()
ilopyu.convert(Qc[0], RQc[0])
print str(RQc) + '\n'

ilopyu.weightspace(RQc[0], Qw, RQw)
print RQw
ilopyu.realWeightValues(RQc[0], RQw,subspace, Rw[0])
print Rw

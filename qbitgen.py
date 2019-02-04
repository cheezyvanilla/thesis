
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
            if RQc[i] == 1:             #not in auto generating Qw
                binbit[i]= {'[ 0.  0.]':np.array([-0.75,0.05]), '[ 0.  1.]':np.array([-0.25,0.05]), '[ 1.  0.]':np.array([0.25,0.05]), '[ 1.  1.]':np.array([0.75,0.05])}[str(RQw[i])]
                Rw[i] = np.random.normal(binbit[i][0],binbit[i][1])

    def qubitUpdate(Qubit, b_best, b, deltaTheta, eps):
        theta = np.zeros((len(b)))
        for i in range(len(b)):
            if b==0 and b_best ==1:
                theta[i] = -deltaTheta
            elif b == 1 and b_best == 0:
                theta[i] = deltaTheta
            else:
                theta[i] = 0
            
            Qubit[i] = (np.cos(theta[i])-np.sin(theta[i]))*Qubit[i]
            if Qubit[i] < np.sqrt(eps):
                Qubit[i] = np.sqrt(eps)
            elif np.sqrt(eps) <= Qubit[i] <= np.sqrt(1-eps):
                Qubit[i] = Qubit[i]
            elif Qubit[i] > np.sqrt(1-eps):
                Qubit[i] = np.sqrt(1-eps)
            


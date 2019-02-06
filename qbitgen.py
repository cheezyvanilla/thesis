
import numpy as np
class qbit():
    def __init__(self, generation, Qc, k):
       self.gen = generation
       self.Qc = Qc
       self.Qw = np.zeros((np.shape(Qc)[0], np.shape(Qc)[1], k))  #Qw or Qw
       for i in range(len(self.Qw)):               #assigning initial qubit value to Qw
            for j in range(len(self.Qw[i])):
                for k in range(len(self.Qw[i][j])):
                    self.Qw[i][j][k] = 1/np.sqrt(2)
    def convert(self, qbit, bin ):                 #real connection value encoding
        r = np.random.sample(len(qbit))
        # print r
        for i in range(len(qbit)):
            if r[i] < qbit[i]**2:
                bin[i]= 1
            else:
                bin[i]= 0
        
    def weightSpaceDef(self,realconvalue, qbit, bin):
        for j in range(len(qbit)):
            for i in range (len(qbit[j])):
                if realconvalue[j][i] == 1:
                    self.convert(qbit[j][i], bin[j][i])
    def realWeightValues(self,RQc, RQw,binbit, Rw): #binbit =binarybit, Rw = real weight values
         for i in range (len(RQc)):
             for j in range(len(RQc[i])):
                if RQc[i][j] == 1:             #not in auto generating Qw
                    binbit[i][j]= {'[ 0.  0.]':np.array([-0.75,0.05]), '[ 0.  1.]':np.array([-0.25,0.05]),\
                         '[ 1.  0.]':np.array([0.25,0.05]), \
                             '[ 1.  1.]':np.array([0.75,0.05])}[str(RQw[i][j])]
                    Rw[i][j] = np.random.normal(binbit[i][j][0],binbit[i][j][1])

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

    def oneTo3(self):
        realConVal = np.zeros((np.shape(self.Qc)))
        realWeiVal = np.copy(realConVal)
        weightSpace = np.zeros((np.shape(self.Qw)))
        subSpace = np.copy(weightSpace)
        for i in range(len(self.Qc))    :
            self.convert(self.Qc[i], realConVal[i])
        self.weightSpaceDef(realConVal, self.Qw, weightSpace)
        #return str(realConVal) +'\n'+ str(weightSpace)
        #self.realWeightValues(realConVal, weightSpace, subSpace, realWeiVal)
        return str(realConVal)+ '\n'+str(weightSpace) #+'\n' + str(realWeiVal)       
            


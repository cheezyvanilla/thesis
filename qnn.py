from qbitgen import qbit
import numpy as np
qbit  = qbit()
generation = 1
Qc = np.zeros((1,2,3))
sqrt2 = 1/np.sqrt(2)
Qc = np.array([[sqrt2, sqrt2,0],[sqrt2, sqrt2, sqrt2]])     #Qc init
deltaTheta = 0.05*np.pi #parameter refinement
eps = 0.005 #parameter refinement
input = np.array([[0,0,0],[0,1,0],[1,0,0],[1,1,0]])
output = np.array([0,1,1,0])
class subpopulasi:
        def __init__(self, Qc):
                self.Qc = Qc
                self.RQc = np.copy(self.Qc)

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
        b = np.array([[edge+(width*i), width*0.1] for i in range(2**self.k)])
        self.z = dict(zip(a,b))
        self.error = 0
        

  #best between individuals

subp3 = [0 for i in range(30)]
subp2 = [0 for i in range(30)]
subp1 = [0 for i in range(30)]
subPop = [0,0,0]

bestSubp = [0 for i in range(3)]
populasi = [subp1, subp2, subp3]

for i in range(len(populasi)):              #INIT INDIVIDUAL OBJECTS
    bestSubp[i] = individual(Qc, 5)
    subPop[i] = subpopulasi(Qc) #init subpopulasi(Qc)
    for j in range(len(populasi[i])):
        populasi[i][j]= individual(Qc,5)


#MAIN LOOP        
for i in range(generation):
    for j in range(len(populasi)):
        qbit.convert(subPop[j].Qc, subPop[j].RQc)
        for k in range(len(populasi[j])):
                populasi[j][k].Qc = subPop[j].Qc
                populasi[j][k].RQc = subPop[j].RQc     #Qc OBSERVATION
                qbit.weightSpaceDef(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].RQw, populasi[j][k].Rw,populasi[j][k].z)
                populasi[j][k].error = qbit.objFunction(populasi[j][k].Rw, input, output)
                if k == 0:
                        bestSubp[j].error = populasi[j][k].error
                        # bestSubp[j].RQc = populasi[j][k].RQc
                        bestSubp[j].RQw = populasi[j][k].RQw
                        bestSubp[j].Rw = populasi[j][k].Rw
                elif populasi[j][k].error > bestSubp[j].error:
                        #update Qw
                        qbit.QwUpdate(populasi[j][k].RQc, populasi[j][k].Qw, bestSubp[j].RQw, populasi[j][k].RQw, deltaTheta, eps)
                        # print 'individu ke {} dari subpopulasi ke {}'.format(k,j)
                        
                        
                        
                        
                else:
                 #       update bestSubp, mean, SD, bestRw, bw(biner)
                        qbit.bestSubUpdate(bestSubp[j], populasi[j][k])
                        # update mean & sd

                
# print bestSubp[0].Rw, bestSubp[0].error
# print bestSubp[1].Rw, bestSubp[1].error
# print bestSubp[2].Rw, bestSubp[2].error




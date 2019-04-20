from xorLib import qbit
import numpy as np
qbit  = qbit()
generation = 2
Qc = np.zeros((1,2,3))
sqrt2 = 1/np.sqrt(2)
Qc = np.array([[1,1]]).astype(float)    #Qc init
deltaTheta = 0.05*np.pi #parameter refinement
eps = 0.005 #parameter refinement
input = np.array([[0,0],[0,1],[1,0],[1,1]])
output = np.array([0,1,1,1])

class individual:
    def __init__(self, Qc, k):
        self.Qc = Qc
        self.Qw = np.zeros((np.shape(self.Qc)[0],np.shape(self.Qc)[1], 5))
        self.Qw.fill(sqrt2)
        self.RQc = np.copy(self.Qc)
        self.RQw = np.copy(self.Qw)
        self.bestRQw = None
        self.Rw = np.copy(self.Qc)
        self.k = k
        width = (float(self.k)/2**self.k)
        edge = -(width*(2**self.k-1)/2)
        a = np.array([i for i in range(2**self.k)])
        b = np.array([[edge+(width*i), width*0.1] for i in range(2**self.k)])
        self.z = dict(zip(a,b))
        self.error = 0
        self.bestError = 0
        

  #best between individuals

subp3 = [0 for i in range(30)]
subp2 = [0 for i in range(30)]
subp1 = [0 for i in range(30)]

bestSubp = [0 for i in range(3)]
populasi = [subp1, subp2, subp3]

for i in range(len(populasi)):              #INIT INDIVIDUAL OBJECTS
    bestSubp[i] = individual(Qc, 5)
    for j in range(len(populasi[i])):
        populasi[i][j]= individual(Qc,5)
naikHaji = [[0,0] for i in range(30)]


iganti = 0
jganti = 0
#MAIN LOOP        
for i in range(generation):
    for j in range(len(populasi)):
            
        for k in range(len(populasi[j])):
                if j == 0 and k == 2:
                    print 'generasi', i
                    print populasi[j][k].bestRQw,populasi[j][k].bestError ,'bestRQw'
                    # print populasi[j][k].RQw,populasi[j][k].error ,'RQw'
                
                qbit.convert(populasi[j][k].Qc, populasi[j][k].RQc)     #Qc OBSERVATION
                qbit.weightSpaceDef(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].RQw, populasi[j][k].Rw,populasi[j][k].z)
                populasi[j][k].error = qbit.objFunction(populasi[j][k].Rw, input, output)
                # print populasi[j][k].RQw,j,k
                if j == 0 and k == 2:
                    print 'generasi', i
                    print populasi[j][k].bestRQw,populasi[j][k].bestError ,'bestRQw'
                if populasi[j][k].bestRQw == None:
                    populasi[j][k].bestRQw = populasi[j][k].RQw 
                    # print populasi[j][k].bestRQw,j,k
                    if j == 0 and k == 2:
                        print 'mengisi bestRQw'
                        print populasi[j][k].RQw
                if i == 0:
                        populasi[j][k].bestError = populasi[j][k].error
                        
                        
                        
                elif populasi[j][k].error > populasi[j][k].bestError:
                        # print populasi[j][k].RQw,j,k, 'update qw'
                        # print populasi[j][k].bestRQw,j,k
                        qbit.QwUpdate(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].bestRQw, populasi[j][k].RQw, deltaTheta, eps)
                        
                elif   populasi[j][k].error == 0:
                    print 'individu terbaik'
                    print populasi[j][k].Rw     
                    break
                elif populasi[j][k].error <= populasi[j][k].bestError:
                 #       update bestInd, mean, SD, bestRw, bw(biner)
                    
                    qbit.bestIndUpdate(populasi[j][k])
                    if j == 0 and k == 2:
                        print 'best individu updated'
                # if j == 0 and k == 2:
                #     print 'generasi', i
                #     print populasi[j][k].bestRQw,populasi[j][k].bestError ,'bestRQw'
                #     print populasi[j][k].RQw,populasi[j][k].error ,'RQw'
                    

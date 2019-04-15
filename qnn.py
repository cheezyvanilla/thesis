from qbitgen import qbit
import numpy as np
qbit  = qbit()
generation = 2
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
                self.Rw = np.copy(self.Qc)
                self.RQc = np.copy(self.Qc)
                self.bestRQc = np.copy(self.Qc)
                self.bestError = 0
                self.error = 0
                self.refinement = 0

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
        self.bestError = 0
        self.bestRQw = np.copy(RQw)
        self.bestRw = np.copy(self.Rw)
        self.refinement = 0
        

  #best between individuals

subp3 = [0 for i in range(30)]
subp2 = [0 for i in range(30)]
subp1 = [0 for i in range(30)]
subPopulation = [0,0,0]

bestIndividual = [0 for i in range(3)]
bestSubPopulation = subpopulasi(Qc)
populasi = [subp1, subp2, subp3]
FInd = [0 for i in range(3)]
FInd[0] = [0 for i in range(30)] #menampung best F untuk subpopulasi
FInd[1] = [0 for i in range(30)]
FInd[2] = [0 for i in range(30)]
for i in range(len(populasi)):              #INIT INDIVIDUAL OBJECTS
    bestIndividual[i] = individual(Qc, 5) #init best individual object in subpopulation
    subPopulation[i] = subpopulasi(Qc) #init subpopulasi(Qc)
    for j in range(len(populasi[i])):
        populasi[i][j]= individual(Qc,5)


#MAIN LOOP        
for i in range(generation):
        for j in range(len(populasi)):
                qbit.convert(subPopulation[j].Qc, subPopulation[j].RQc)  #Qc OBSERVATION
                for k in range(len(populasi[j])):
                        populasi[j][k].Qc = subPopulation[j].Qc
                        populasi[j][k].RQc = subPopulation[j].RQc     
                        qbit.weightSpaceDef(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].RQw, populasi[j][k].Rw,populasi[j][k].z)
                        populasi[j][k].error = qbit.objFunction(populasi[j][k].Rw, input, output)
                        if i == 0:
                                populasi[j][k].bestError = populasi[j][k].error
                                # bestIndividual[j].RQc = populasi[j][k].RQc
                                populasi[j][k].bestRQw = populasi[j][k].RQw
                                populasi[j][k].bestRw = populasi[j][k].Rw
                        elif populasi[j][k].error > populasi[j][k].bestError:
                                #update Qw
                                qbit.QwUpdate(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].bestRQw, populasi[j][k].RQw, deltaTheta, eps)
                                
                                
                                
                                
                                
                        else:
                        #       update bestIndividual, mean, SD, bestRw, bw(biner)
                                qbit.bestIndUpdate(populasi[j][k])
                                
                if i == 0:
                        
                        for wew in range(len(FInd)):

                                FInd[wew] = populasi[j][wew].bestError
                        subPopulation[j].bestError = min(FInd)



                elif bestIndividual[j].error >= bestSubPopulation.error:
                                #update subpopulation[j]s
                                # print bestIndividual[j].RQc, "best individu"
                                # print bestSubPopulation.RQc, "best subp"
                                qbit.QcUpdate(subPopulation[j].RQc, bestSubPopulation.RQc, subPopulation[j].Qc, deltaTheta, eps)
                                
                else:
                                qbit.bestSubPopUpdate(bestIndividual[j], bestSubPopulation) #update best subpopulation
                                print 'best subpopulasi update'
        # if (i+1)%5==0:
        #         qbit.weightExchange(populasi)
        #         # print "exchange done"
        # if (i+1)%10 ==0:
        #         qbit.connExchange(subPopulation)
        print subPopulation[0].Qc
        print subPopulation[0].RQc
        print subPopulation[1].Qc
        print subPopulation[1].RQc
        print subPopulation[2].Qc
        print subPopulation[2].RQc
        print bestSubPopulation.RQc
# print populasi[0][0].Qc, subPopulation[0].refinement
# print populasi[1][0].Qc, subPopulation[0].refinement
# print populasi[2][0].Qc, subPopulation[0].refinement




from qbitgen import qbit
import numpy as np
qbit  = qbit()
generation = 2000
layer = [4,6,1]
Qc = qbit.netGen(4,6,1)     #Qc init
# Qc = np.array([[1,1,1, 0],[1,1,1,1]])
# Qc = np.array([[1, 1,0],[1, 1, 1]]) 
sqrt2 = 1/np.sqrt(2)
deltaTheta = 0.05*np.pi #parameter refinement
eps = 0.005 #parameter refinement
input = np.array([[94, 87, 78, 87],[92, 131,74,68],[100,177,126,78],[110,153, 101, 77],[82, 145,99,67],[82, 191, 102, 87],[92, 141, 76, 78],[91,112,65,82],[98,154,100,85],[86,88, 67, 89],[90, 175, 120, 83],[87,139,100,80],[84, 119, 60,67],[87,76,58,80],[80,110,86,90],[110,207,147,84],[79, 125, 78,71],[89,165,136,90],[82, 143,99,82],[84, 137, 90,67],[92,131,102,90],[86,171,135,79],[79,157,138,89],[75,96,71,85],[79,126,78,67],[82,135,79,78],[85,128,76,85],[91,158,117,89],[90,130,102,80],[75,141,90,65],[105,180,129,84],[82,131,99,68],[85,121,95,82],[79,166,122,75],[78,115,72,76],[90,163,110,77],[85,149,84,67],[92,133,97,89],[85,126,86,85],[95, 163,117,71],[93,106,71,85],[82,152,112,66],[89,108,76,86],[100,162,93,78],[88,136,105,75]])
output = np.array([6.4e-2,4.3e-2, 2.5e-2, 3.3e-2, 3.4e-2, 2.0e-2, 4.5e-2,5.5e-2, 3.2e-2, 7.2e-2, 2.3e-2, 3.5e-2, 4.9e-2, 7.8e-2, 6.2e-2, 1.7e-2, 4.9e-2, 1.9e-2, 3.5e-2, 3.8e-2, 3.2e-2, 2.4e-2, 1.9e-2, 7.4e-2, 4.9e-2, 5.1e-2, 4.8e-2, 2.6e-2, 3.8e-2, 3.7e-2, 2.1e-2, 3.5e-2, 3.8e-2, 2.4e-2, 5.5e-2, 2.7e-2, 4.0e-2, 3.3e-2, 4.5e-2, 2.4e-2, 5.8e-2, 2.9e-2, 6.0e-2, 3.5e-2, 3.7e-2])

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
        self.bestRQw = None
        
        
        

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
                
                # print subPopulation[j].RQc == subPopulation[j].bestRQc
                for k in range(len(populasi[j])):
                        populasi[j][k].Qc = np.copy(subPopulation[j].Qc)
                        populasi[j][k].RQc = np.copy(subPopulation[j].RQc)     
                        qbit.weightSpaceDef(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].RQw, populasi[j][k].Rw,populasi[j][k].z)
                        populasi[j][k].error = qbit.objFunction(populasi[j][k].Rw,layer , input, output)
                        if populasi[j][k].bestRQw == None:
                            populasi[j][k].bestRQw = np.copy(populasi[j][k].RQw) #THE PROBLEM IS HERE
                            # print populasi[j][k].bestRQw,j,k
                    
                        if i == 0:
                                populasi[j][k].bestError = np.copy(populasi[j][k].error)

                        elif populasi[j][k].error > populasi[j][k].bestError:
                                #update Qw
                                qbit.QwUpdate(populasi[j][k].RQc, populasi[j][k].Qw, populasi[j][k].bestRQw, populasi[j][k].RQw, deltaTheta, eps)
                                # print 'Qw Update'
                        elif   populasi[j][k].error == 0:
                            print 'individu terbaik di populasi {} individu {} found in generation {}'.format(j,k,i)
                        #     print populasi[j][k].Rw 
                              
                        #     break        
                                
                        else:
                        #       update bestIndividual, mean, SD, bestRw, bw(biner)
                                qbit.bestIndUpdate(populasi[j][k])

                # print 'best in subpop {},min F = {}'.format(subPopulation[j].bestError, min(FInd[j]))
                # print subPopulation[j].bestError== min(FInd[j])
                for wew in range(len(FInd[j])):                         #store all individuals error
                                FInd[j][wew] = np.copy(populasi[j][wew].bestError)    
                # print FInd[j]                            
                # print FInd[j], min(FInd[j])
                # print min(FInd[j]),subPopulation[j].bestError,'best indiv, pop ke', j
                if i == 0:                        
                        subPopulation[j].bestError = np.copy(min(FInd[j]))
                        subPopulation[j].bestRQc = np.copy(subPopulation[j].RQc)

                        # print 'store value to best variable'
                        # print subPopulation[j].bestError
                elif min(FInd[j]) > subPopulation[j].bestError:
                                
                                qbit.QcUpdate(subPopulation[j], deltaTheta, eps)
                                print 'Qc Updating'
                                
                else:
                                # print 'update populasi pada subpop ke ', j
                                # print subPopulation[j].bestRQc,'awal'
                                
                                qbit.subPopUpdate(subPopulation[j], min(FInd[j])) #update best subpopulation
                                # print 'subpop updated'
                # print subPopulation[j].bestError               
                print subPopulation[j].bestError               
        if (i+1)%5==0:
                qbit.weightExchange(populasi)
                # print "exchange done"
        if (i+1)%10 ==0:
                qbit.connExchange(subPopulation)
print 'sub 1'
print FInd[0]
print 'sub 2'
print FInd[1]
print 'sub3'
print FInd[2]
print subPopulation[0].bestError
print subPopulation[1].bestError
print subPopulation[2].bestError


import numpy as np
class qbit():
    def __init__(self):
        return None
    def convert(self, qbit, bin ):                 #real connection value encoding
        for i in range(len(qbit)):
            r = np.random.sample(len(qbit[i]))
            # print r
            for j in range(len(qbit[i])):
                if r[j] < qbit[i][j]**2:
                    bin[i][j]= 1
                else:
                    bin[i][j]= 0
            
        # print r
        
    # def weightSpaceDef(self,realconvalue, qbit, bin):
    #     for k in range(len(realconvalue)):
    #         for j in range(len(realconvalue[k])):
    #             for i in range (len(realconvalue[k][j])):
    #                 if realconvalue[k][j][i] == 1:
    #                     self.convert(qbit[k][j], bin[k][j])
    def weightSpaceDef(self,realconvalue, qbit, bin, Rw, z):
        
        for j in range(len(realconvalue)):
            for i in range (len(realconvalue[j])):
                if realconvalue[j][i] == 1: 
                    r = np.random.sample(len(qbit[j][i]))
                    for k in range(len(qbit[j][i])):
                            if r[k] < qbit[j][i][k]**2:
                                bin[j][i][k]= 1
                            else:
                                bin[j][i][k]= 0
                    y = bin[j][i]
                    subs = z[int(''.join(map(lambda y: str(int(y)), y)),2)]
                    Rw[j][i] = np.random.normal(subs[0], subs[1]) 
                    # print(int(''.join(map(lambda y: str(int(y)), y)),2) )
                else:
                    Rw[j][i]= 0
    def QcUpdate(self, RQc, best_RQc, Qc, deltaTheta,eps):
        theta = deltaTheta
         
        for i in range(len(RQc)):
             for j in range(len(RQc[i])):
                if RQc[i][j]==0 and best_RQc[i][j]==1:
                     theta = -deltaTheta
                     
                elif RQc[i][j]==1 and best_RQc[i][j]==0:
                    theta = deltaTheta
                else:
                    theta = 0
                Qc[i][j] =np.dot(np.array([np.cos(theta), -np.sin(theta)]), \
                                np.array([Qc[i][j], np.sqrt(1- (Qc[i][j])**2)]))
                # print Qc[i][j], theta
                if Qc[i][j] < np.sqrt(eps):
                        Qc[i][j] = np.sqrt(eps)
                elif np.sqrt(eps) <= Qc[i][j] <= np.sqrt(1-eps):
                        Qc[i][j] = Qc[i][j]
                        
                elif Qc[i][j] > np.sqrt(1-eps):
                        Qc[i][j] = np.sqrt(1-eps)
        # print Qc

                
    

    def QwUpdate(self, realConValue, Qubit, b_best, b, deltaTheta, eps):
        theta = deltaTheta
        for i in range(len(realConValue)):
            for j in range(len(realConValue[i])):
              if realConValue[i][j] == 1 :  
                for k in range(len(b[i][j])):
                    if b[i][j][k]==0 and b_best[i][j][k] ==1:
                        theta = -deltaTheta
                    elif b[i][j][k] == 1 and b_best[i][j][k] == 0:
                        theta = deltaTheta
                    else:
                        theta = 0
                    
                    Qubit[i][j][k] =np.dot(np.array([np.cos(theta), -np.sin(theta)]), \
                                np.array([Qubit[i][j][k], np.sqrt(1- (Qubit[i][j][k])**2)]))
                    # print 'qbit indeks[{}][{}][{}]'.format(i,j,k), Qubit[i][j][k], theta
                    if Qubit[i][j][k] < np.sqrt(eps):
                        Qubit[i][j][k] = np.sqrt(eps)
                    elif np.sqrt(eps) <= Qubit[i][j][k] <= np.sqrt(1-eps):
                         Qubit[i][j][k] = Qubit[i][j][k]
                    elif Qubit[i][j][k] > np.sqrt(1-eps):
                        Qubit[i][j][k] = np.sqrt(1-eps)
    def bestIndUpdate(self, populasi):
        populasi.bestError = populasi.error
        populasi.bestRQw = populasi.RQw
        populasi.bestRw = populasi.Rw
        # bestSub.RQc = populasi.RQc
        for j in range(len(populasi.RQc)):
            for i in range (len(populasi.RQc[j])):
                if populasi.RQc[j][i] == 1: 
                    y = populasi.RQw[j][i]

                    populasi.z[int(''.join(map(lambda y: str(int(y)), y)),2)][0] = populasi.Rw[j][i]
                    populasi.z[int(''.join(map(lambda y: str(int(y)), y)),2)][1] = populasi.z[int(''.join(map(lambda y: str(int(y)), y)),2)][1]*0.8
                    
    def bestSubPopUpdate(self, bestSubPop, subPop):
        bestSubPop.error = subPop.error
        bestSubPop.RQc = subPop.RQc
        bestSubPop.Rw = subPop.Rw
    def actFunc(self,x):
        return (1/(1+np.exp(-x))).astype(float)
    def objFunction(self, net, x, y):
        er= 0
        for i in range(len(x)):
            h = np.dot(x[i],net[0])
            x2 = np.copy(x[i]).astype(float)
            x2[2]= self.actFunc(h)
            a = np.dot(x2, net[1])  #output program
            
            if a < 0 :
                z = 0
            else:
                z = 1
           
            if z!= y[i]:
                er +=1
        return er 

    def weightExchange(self, objek):
        for ha in range(len(objek)):
            a = [0 for i in range(len(objek[ha]))]
            for j in range(len(objek[ha])):
                a[j] = objek[ha][j].Qw
            np.random.shuffle(a)
            for k in range(len(objek[ha])):
                objek[ha][k].Qw = a[k] 
    def connExchange(self,objek):
        a = [0 for i in range(len(objek))]
        for j in range(len(objek)):
            a[j] = objek[j].Qc
        
        np.random.shuffle(a)
        
        for k in range(len(objek)):
            objek[k].Qc = a[k]
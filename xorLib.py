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
        
                
    def realWeightValues(self,RQc, RQw,binbit, Rw): #binbit =binarybit, Rw = real weight values
        width = (float(self.k)/2**self.k)
        edge = -(width*(2**self.k-1)/2)
        a = np.array([i for i in range(2**self.k)])
        b = np.array([edge+(width*i) for i in range(2**self.k)])
        z = dict(zip(a,b))
        #print z
        #realWeiVal = np.copy(RQc)
        for i in range (len(RQc)):
             for j in range(len(RQc[i])):
                if RQc[i][j] == 1:             
                    y = RQw[i][j]
                    Rw[i][j]= z[int(''.join(map(lambda y: str(int(y)), y)),2)]

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

                    if Qubit[i][j][k] < np.sqrt(eps):
                        Qubit[i][j][k] = np.sqrt(eps)
                    elif np.sqrt(eps) <= Qubit[i][j][k] <= np.sqrt(1-eps):
                        continue
                        # Qubit[i][j][k] = Qubit[i][j][k]
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

    def objFunction(self, net, x, y):    #or gate
        er= 0
        for i in range(len(x)):
            h = np.dot(x[i],net[0])
            x2 = np.copy(x[i]).astype(float)
            x2[2]= h 
            a = np.dot(x2, net[1])  #output program
            
            if a < 0 :
                z = 0
            else:
                z = 1
           
            if z!= y[i]:
                er +=1
        return er
    def objFunction(self, net, x, y):    #or gate
        er= 0
        for i in range(len(x)):
            h = np.dot(x[i],net[0])
            if h<0:
                h = 0
            else:
                h = 1
            if h != y[i]:
                er+=1
        return er

              

            
                # print a,z , y[i]
            
        #     if z != y[i]:
        #         error+=1
        # return error

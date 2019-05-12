
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
                    Rw[j][i] = float(np.random.normal(subs[0], subs[1]) )
                    # print(int(''.join(map(lambda y: str(int(y)), y)),2) )
                    # print np.random.normal(subs[0], subs[1])
                    # print Rw[j][i], "Rw" 
                else:
                    Rw[j][i]= 0
    def QcUpdate(self, subpopulasi, deltaTheta,eps):
        theta = np.copy(deltaTheta)
         
        for i in range(len(subpopulasi.RQc)):
             for j in range(len(subpopulasi.RQc[i])):
                if subpopulasi.RQc[i][j]==0 and subpopulasi.bestRQc[i][j]==1:
                     theta = -deltaTheta
                     
                elif subpopulasi.RQc[i][j]==1 and subpopulasi.bestRQc[i][j]==0:
                    theta = deltaTheta
                else:
                    theta = 0
                subpopulasi.Qc[i][j] =np.dot(np.array([np.cos(theta), -np.sin(theta)]), \
                                np.array([subpopulasi.Qc[i][j], np.sqrt(1- (subpopulasi.Qc[i][j])**2)]))
                # print Qc[i][j], theta
                if subpopulasi.Qc[i][j] < np.sqrt(eps):
                        subpopulasi.Qc[i][j] = np.sqrt(eps)
                elif np.sqrt(eps) <= subpopulasi.Qc[i][j] <= np.sqrt(1-eps):
                        subpopulasi.Qc[i][j] = subpopulasi.Qc[i][j]
                        
                elif subpopulasi.Qc[i][j] > np.sqrt(1-eps):
                        subpopulasi.Qc[i][j] = np.sqrt(1-eps)
        # print Qc

                
    

    def QwUpdate(self, realConValue, Qubit, b_best, b, deltaTheta, eps):
        theta = deltaTheta
        for i in range(len(realConValue)):
            for j in range(len(realConValue[i])):
              if realConValue[i][j] == 1 :  
                for k in range(len(b[i][j])):
                    if b[i][j][k]==0 and b_best[i][j][k] ==1:
                        theta = -deltaTheta
                        # print 'brubah'
                    elif b[i][j][k] == 1 and b_best[i][j][k] == 0:
                        theta = deltaTheta
                        # print 'berubah'
                    else:
                        theta = 0
                        # print 'tidak berubah'
                    
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
        populasi.bestError = np.copy(populasi.error)
        populasi.bestRQw = np.copy(populasi.RQw)
        populasi.bestRw = np.copy(populasi.Rw)
        # bestSub.RQc = populasi.RQc
        for j in range(len(populasi.RQc)):
            for i in range (len(populasi.RQc[j])):
                if populasi.RQc[j][i] == 1: 
                    y = populasi.RQw[j][i]

                    populasi.z[int(''.join(map(lambda y: str(int(y)), y)),2)][0] = populasi.Rw[j][i]
                    populasi.z[int(''.join(map(lambda y: str(int(y)), y)),2)][1] = populasi.z[int(''.join(map(lambda y: str(int(y)), y)),2)][1]*0.8
                    # print populasi.Rw[j][i]
    def subPopUpdate(self, subPop, minF):
        subPop.bestError = np.copy(minF)
        subPop.bestRQc = np.copy(subPop.RQc)
        # bestSubPop.Rw = subPop.Rw
    
   



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


    def objFunction(self, net,x,out):    #or gate
        h = 0
        p = 0
        y = 0
        er = 0
        for i in range(len(x)):
            h = np.dot(net[0],x[i])

            # p = np.append(x[i], 1/(1+np.exp(-h))).astype(float)
            # p = np.append(x[i], 0 if h<0 else 1).astype(float)
            x[i][3] = 0 if h<0 else 1
            
            y = np.dot(net[1], x[i])
            y = 0 if y< 0 else 1
            if out[i] == y:
                er +=0
            else : 
                er +=1
        return er
    # def objFunction(self, net, x, y):
    #     er= 0
    #     z = 0
    #     for i in range(len(x)):
    #         h = np.dot(x[i],net[0])
    #         if h < 0 :
    #             h = 0
    #         else:
    #             h = 1
           
    #         if z!= y[i]:
    #             er +=1
    #         x2 = np.copy(x[i]).astype(float)
    #         x2[2]= (h)
    #         a = np.dot(x2, net[1])  #output program
            
    #         if a < 0 :
    #             z = 0
    #         else:
    #             z = 1
           
    #         if z!= y[i]:
    #             er +=1
    #     return er 
    # def objFunction(self, net, x, y):    #or gate
    #     er= 0
    #     for i in range(len(x)):
    #         h = np.dot(x[i],net[0])
    #         if h<0:
    #             h = 0
    #         else:
    #             h = 1
    #         if h != y[i]:
    #             er+=1
    #     return er
    def netGen(self, input, hidden, output):
        net = np.zeros((input+hidden+output,input+hidden+output))
        for i in range(input+hidden+output): 
            for j in  range(input+hidden+output):
                for hid in range(hidden):
                    if i>(input-1)+hid and j <input+hid:
                        net[i][j] = 1/np.sqrt(2)

                if i>(input+hidden-1) and j<(input+hidden):
                    net[i][j] = 1/np.sqrt(2)
        return net
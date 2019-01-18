import numpy as np
class qbit():
    def __init__(self):
       return None
    def convert(self, qbit, bin ):                 #real connection value encoding
        r = np.random.sample(len(qbit))
        #print r
        for i in range(len(qbit)):
            if r[i] < qbit[i]**2:
                bin[i]= 1
            else:
                bin[i]= 0
        return 0
    def weightspace(self,realconvalue, qbit, bin):
        for i in range (len(realconvalue)):
            if realconvalue[i] == 1:
                 z =np.random.sample(2)
                 print z
                 for j in range(2):
                     if z[j]< 0.5:
                         print z[j]
                         bin[i][j] = 1
                     else:
                         bin[i][j] = 0


    # def weigh(self, obj, mean, SD):      #weighing the connection
    #     for i in range(len(obj)):
    #         if obj[0][i] == 1:
    #             s[0][i] = 

#init       
Qc = np.zeros((3,3))
Qw = np.zeros((3,2))
Qw[0] = Qw[1] =Qw[2]= np.array([[1/np.sqrt(2), 1/np.sqrt(2)]])
RQw =np.zeros((3,2))
Qc[0] = np.array([1/np.sqrt(2), 1/np.sqrt(2), 1/np.sqrt(2)])

RQc = np.zeros((3,3))
s = np.zeros((3,3))

#main
ilopyu = qbit()
ilopyu.convert(Qc[0], RQc[0])
print str(RQc) + '\n'

ilopyu.weightspace(RQc[0], Qw, RQw)
print RQw


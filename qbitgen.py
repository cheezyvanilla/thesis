import numpy as np
class qbit():
    def __init__(self):
       return None
    def convert(self, obj):
        r = np.random.sample(3)
        print r
        for i in range(len(obj)):
            if r[i] < obj[i]**2:
                RQc[0][i]= 1
            else:
                RQc[0][i]= 0
        return 0
Qc = np.zeros((3,3))
Qc[0] = np.array([1/np.sqrt(2), 1/np.sqrt(2), 1/np.sqrt(2)])
RQc = np.zeros((3,3))

print RQc
ilopyu = qbit()
ilopyu.convert(Qc[0])
print RQc


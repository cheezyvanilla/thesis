from qbitgen import qbit
import numpy as np
Qc=np.zeros((3,3))
sqrt2 = 1/np.sqrt(2)
Qc[0]=Qc[1] = Qc[2]= np.array([sqrt2, sqrt2, sqrt2])
qb = qbit(100, Qc,3)
print qb.oneTo3()
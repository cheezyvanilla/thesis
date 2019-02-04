from qbitgen import qbit
import numpy as np
sqrt2 = 1/np.sqrt(2)
Qc = np.zeros((3,3)) #network Qconnection
Qw = np.zeros((3,3)) #network Qweight
Qw[0] = Qw[1] =Qw[2]= np.array([[sqrt2, sqrt2, sqrt2]])
RQw =np.zeros((3,3)) #realbit weight
Qc[0] = np.array([sqrt2, sqrt2, sqrt2])

RQc = np.zeros((3,3)) #real connection
s = np.zeros((3,3))

subspace = np.zeros((3,2)) #binarybit of subspace values
Rw = np.zeros((1,3))
#main
ilopyu = qbit()
ilopyu.convert(Qc[0], RQc[0])
print str(RQc) + '\n'

ilopyu.weightspace(RQc[0], Qw, RQw)
print RQw
# ilopyu.realWeightValues(RQc[0], RQw,subspace, Rw[0])
# print Rw
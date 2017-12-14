####################################

#Created by: Simsarul Haq Vengasseri
#Date: 14/12/2017

# This program is for grover search algorithm
# Please specify the path to the referenceqvm directory to import the api library.



import sys
sys.path.insert(0, '/home/simsar/Desktop/QSims/reference-qvm/referenceqvm')
import api
import pyquil.quil as pq
from pyquil.gates import *

qvm = api.SyncConnection()

p = pq.Program()
p.inst(H(1),H(2))

search = 1
array = [1,0,0,0]

if (array == [0,0,0,1]):
    p.inst(H(2),CNOT(1,2),H(2))
    qbits, addr = qvm.wavefunction(p, [0,1])
    print qbits
elif (array == [0,1,0,0]):
    p.inst(H(2),CNOT(1,2),H(2),X(1))
    qbits, addr = qvm.wavefunction(p, [0,1])
    print qbits
elif (array == [0,0,1,0]):
    p.inst(H(2),CNOT(1,2),H(2),X(2))
    qbits, addr = qvm.wavefunction(p, [0,1])
    print qbits
elif (array == [1,0,0,0]):
    p.inst(H(2),CNOT(1,2),H(2),X(1),X(2))
    qbits, addr = qvm.wavefunction(p, [0,1])
    print qbits

p.inst(H(1),H(2),X(1),X(2),H(2),CNOT(1,2),H(2),X(1),X(2),H(1),H(2))
p.measure(1,0).measure(2,1)
qbits, addr = qvm.wavefunction(p, [0,1])

print addr

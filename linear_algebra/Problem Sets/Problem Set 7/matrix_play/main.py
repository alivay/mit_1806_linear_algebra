import numpy as np
from numpy import linalg as LA

A=np.random.randint(10, size=(3,3))-5

print(A)
eigenvalues = LA.eigh(A)[0]
print(eigenvalues)
eye = np.eye(3, dtype=int)
print(eye)
print(A-eigenvalues[0]*eye)

x = np.linalg.solve(A-eigenvalues[0]*eye,np.zeros(3).reshape(3,1))
print(x)

print(np.matmul(A,x))
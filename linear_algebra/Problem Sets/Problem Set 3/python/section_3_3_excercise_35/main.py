import numpy as np
import matplotlib.pyplot as plt

K = np.zeros((9, 9))

K[0,0]=2
for i in range(0,8):
    K[i+1,i+1]=2
    K[i+1,i]=-1
    K[i, i+1] = -1
print(K)

b=10*np.ones((9,1))
print(b)

base =[i for i in range(1,10)]
x= np.matmul(np.linalg.inv(K),b)

plt.plot(base, x)
plt.show()

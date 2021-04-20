import numpy as np
import matplotlib.pyplot as plt
print("hello world")

u1 = []
u2 = []

a = np.array([[0.8, 0.3],
              [0.2, 0.7]])

b = np.array([[0],
              [1]])

rr=range(0,8)

for i in rr:
    print("u{}:".format(i))
    print("{}".format(b))
    u1.append(b[0,0])
    u2.append(b[1,0])
    print("u1 = {}".format(u1))
    b=np.matmul(a, b)



print("rr = {}".format(rr))
print("u1 = {}".format(u1))
print("u2 = {}".format(u2))
plt.plot(rr, u1, color='r')
plt.plot(rr, u2, color='b')
plt.title("n vs u1 and u2")
plt.legend(["u1","u2"],  loc="upper right")
plt.xlabel("n")
plt.ylabel("u1&u2")
plt.show()
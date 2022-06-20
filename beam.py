import math
import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
#
a = 1e0
E = 1e0
I = 1e0
mu = 1e0
L = 1e0
#
dx=1e-3
#
m = 4
#
B = []
#
for i in range(m):
    B.append(math.pi/L+math.pi*(i)/L)
#
B = np.array(B)
#
x = np.arange(0,L+dx,dx)
#
v = np.zeros((m,len(x)))
for i in range(m):
    v[i][:] = a*np.sin(B[i]*x)
#
fig, ax = plt.subplots(m)
for i in range(m):
    ax[i].plot(x,v[i])
#
fig.tight_layout()
#
plt.show()
#

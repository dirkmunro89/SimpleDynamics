import math
import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
#
A = 50.
I = 1000.
l = 500.
E = 2.e6
p = 0.784
l_f = math.pi/l*9
w_f = np.sqrt((E*I*l_f**4.)/(p*A))
print(2*math.pi*1.405)
print(w_f)
#
m = 50
#
l_n = []
w_n = []
D_n = []
c=0
for n in range(1,m,2):
    l_n.append(math.pi*n/l)
    w_n.append(np.sqrt((E*I*l_n[c]**4.)/(p*A)))
    D_n.append(np.array([[0., w_n[c]**2.],[-1.,0.]]))
    c=c+1
print(w_n[0])
#
t0=0.
te=15.
dlt=1e-6
time = np.arange(t0,te,dlt)
#
Q=np.array([[0.],[0.]]) # relative velocity and disp.
#
p1=[]
p2=[]
#
for t in time:
#
    c=0
    F_n=[]
    ac = -w_f**2.*np.sin(w_f*t)#*np.exp(-t/w)
    for n in range(1,m,2):
        F_n.append(np.array([[-4./math.pi/n*ac],[0.]]))
        Qdot = F_n[c] - D_n[c].dot(Q)
        Q = Q + Qdot*dlt*np.sin(l_n[c]*l/2.)
        c=c+1
#
    p1.append(Q[1])
    p2.append(ac)
#
fig, ax = plt.subplots(1)
ax.plot(time,p1)
ax.plot(time,p2)
#ax[0].title.set_text('Accelerations')
ax.legend(['p1','p2'])
#fig.tight_layout()
#
plt.show()
#

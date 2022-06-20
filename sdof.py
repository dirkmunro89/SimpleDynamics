import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
#
m = 2.0 # mass
k = 2.0 # stiffness
b = 0.0 # damping
#
w = 2.0 # freq. of forced acceleration
#
D = np.array([[b/m, k/m],[-1.,0.]])
#
t0=0.
te=50.
dlt=1e-3
time = np.arange(t0,te, dlt)
#
Y=np.array([[0.],[0.]]) # relative velocity and disp.
#
p11=[]
p12=[]
p21=[]
p22=[]
#
e = []
#
for t in time:
#
    a1 = 1e0#*np.cos(w*t)#*np.exp(-t/w) # absolute acceleration of driving body
    if t > 10:
        a1 = 0e0
    F = np.array([[-a1],[0.]])
#
    Ydot = F - D.dot(Y) # relative acceleration and velocity
    Y = Y + Ydot*dlt # update of relative velocity and disp.
    a2 = Ydot[0] + a1 # absolute acceleration of body
#
    ke = 0.5* m * Y[0]**2
    pe = 0.5* m * Y[1]**2
#
#   for plotting
    p11.append(a1)
    p12.append(a2)
    p21.append(Y[0])
    p22.append(Y[1])
    e.append(ke+pe)
#
fig, ax = plt.subplots(3)
ax[0].plot(time,p11)
ax[0].plot(time,p12)
ax[0].title.set_text('Accelerations')
ax[0].legend(['a1','a2'])
ax[1].plot(time,p21)
ax[1].plot(time,p22)
ax[1].title.set_text('Displacement and velocity')
ax[1].legend(['rel. velocity','rel. displacement'])
ax[2].plot(time,e)
ax[2].title.set_text('Total energy (state-space)')
fig.tight_layout()
#
print('Critical damping:', np.sqrt((-b**2. + 4.*m*k)/2./m))
print('Natural frequency:',np.sqrt(k/m))
#
plt.show()
#

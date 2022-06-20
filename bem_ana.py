import math
import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
#
def qun(x,t,m,l_n,w_n,s_n,w_f):
#
    c=0
    u = 0.
    for n in range(1,m,2):
#
        w_d = w_n[c]*np.sqrt(1.-s_n[c]**2.)
#
        D_n = (w_n[c]**2. - w_f**2.)**2. + 4.*(s_n[c]*w_n[c]*w_f)**2.
        C1_n = (-8.*s_n[c]*w_f*w_n[c]**3.)/n/math.pi/D_n
        C2_n = (4.*w_f**2.)/(n*math.pi*D_n)*((1.-4.*s_n[c]**4.)*w_n[c]**2. - w_f**2.)
#
        q_n = C1_n*(np.cos(w_f*t)-np.exp(-s_n[c]*w_n[c]*t)*(np.cos(w_d*t)+s_n[c]*w_n[c]/w_d*np.sin(w_d*t)))
        q_n = q_n + C2_n*(np.sin(w_f*t) - np.exp(-s_n[c]*w_n[c]*t)*np.sin(w_d*t))
#
        Y_n = np.sin(l_n[c]*x)
#
        c=c+1
#
        u = u + q_n*Y_n
#
    f = np.sin(w_f*t)
    y = f + u
#
    return y
#
if __name__ == "__main__":
#
    A=50.
    l=500.
    p=0.784
    I=1000.
    E=1.96e9
    B=0.
#
    m=10
#
    l_n=[]
    w_n=[]
    s_n=[]
    for n in range(1,m,2):
#
        tmp=n*math.pi/l
        l_n.append(tmp)
        tmp=np.sqrt((E*I*l_n[-1]**4.)/p/A)
        w_n.append(tmp)
        tmp=B/2./p/A/w_n[-1]
        tmp=0.02
        s_n.append(tmp)
#
    w_f=w_n[0]*2.95
    print(w_n[0]/2/math.pi)
#
    f=[]
    t0=0.
    dlt=1e-4
    te=2.*math.pi/w_n[0]*21.
    time = np.arange(t0,te,dlt)
    for t in time:
        f.append(qun(l/2.,t,m,l_n,w_n,s_n,w_f))
#
    fig, ax = plt.subplots(1)
    ax.plot(time,f)
#
    plt.show()
#

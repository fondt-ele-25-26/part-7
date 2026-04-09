import numpy as np
from scipy import integrate

def q(t, a=4, b=2, c=1):
    return a + b * np.sin(2*np.pi*t/24) + c * np.sin(2*np.pi*t/13)

def immissione(f, t0, t1):
    Q, eb = integrate.quad(f, t0, t1)
    return Q


import numpy as np
from scipy import integrate

def posizione(t, v0=3.8, h0=2, g=9.80665, c=0.023):
    x0 = v0 * t
    x1 = h0 - 0.5 * c * g * t**2
    return x0, x1

def velocita(t, v0=3.8, g=9.80665, c=0.023):
    dx0 = v0 * t**0
    dx1 = - c * g * t
    return dx0, dx1

def lvel(t, v0=3.8, g=9.80665, c=0.023):
    dx0, dx1 = velocita(t, v0, g, c)
    return np.sqrt(dx0**2 + dx1**2)

def lunghezza(t0, t1, v0=3.8, g=9.80665, c=0.023):
    L, error_ub = integrate.quad(lvel, t0, t1)
    return L

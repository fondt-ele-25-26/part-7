from scipy import integrate

def v(x, a=-0.5, b=2, c=0.4):
    return a*x**2 + b*x + c


def media(f, x0, x1):
    vm, error_ub = integrate.quad(f, x0, x1)
    return vm / (x1 - x0)

"""
A bright soliton in 1D.
"""

from fluxion import *

t = PropagationDimension('t')
x = TransverseDimension.uniform('x', 0, 20, 100)
psi = UnknownField('psi', x, t, kind=COMPLEX)

eq = Eq(diff(psi, t), 0.5j * diff(psi, x**2) + (1j * abs(psi) - 0.5j) * psi)

def xdensity(psi, t):
    return abs(psi)**2

k = momentum_space(x)
def kdensity(psi, t):
    return abs(to_momentum_space(psi, x, k))**2

psi0 = 1 / cosh(x)
results = integrate(
    eq, psi0, 0,
    samplers=dict(
        xdensity=(xdensity, linspace(0, 5, 101)),
        kdensity=(kdensity, linspace(0, 5, 101))))

plot(results)

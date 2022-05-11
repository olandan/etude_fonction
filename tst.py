from courbe_TeX import *

from sympy import symbols, exp, sqrt, cos, sin
from matplotlib.pyplot import show

x = symbols('x')

f = Fonction(x,exp(x)+sqrt(x)-2,-4,4)

# Calcul de f(4)
print(f._x(4))

# Calcul de f'(4)
print(f.der(4))

# Affichage de la courbe
f.courbe()
show()

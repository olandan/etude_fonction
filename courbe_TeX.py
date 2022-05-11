# Bibliothèque étudiant une fonction

from sympy import lambdify, diff
from matplotlib.pyplot import subplots, xlim, ylim, plot
from numpy import arange


class Fonction:

    # Définition de la classe
    def __init__(self, var, expression, x_min, x_max):

        # Variable
        self.x = var
        # Borne inférieure intervalle
        self.x_min = x_min
        # Borne supérieure intervalle
        self.x_max = x_max
        # Expression de la fonction
        self._x = lambdify(self.x,expression)
        # Expression de la dérivée
        self.der = lambdify(self.x,diff(expression,self.x))

    # Courbe de la fonction
    def courbe(self,X_grad = 1, Y_grad = 1, x_grad = 1, y_grad = 1):

        # Initialisation de la figure
        fig, ax = subplots(figsize = [5,5], dpi = 200.0)

        # Valeurs en abscisse et ordonnée
        X = [self.x_min + k*(self.x_max - self.x_min)/1000 for k in range(1001)]
        Y = [self._x(x) for x in X]

        # Borne de la représentation
        xlim(min(0,self.x_min),max(0,self.x_max))
        ylim(min(0,min(Y)),max(0,max(Y)))

        # Placement des axes
        # Côté droit et haut du cadre invisibles
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        # Placer le bord du bas en y=0
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data',0))
        # Placer le bod de gauche en x=0:
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data',0))

        # Création des grilles
        ax.set_xticks(arange(self.x_min,self.x_max,x_grad), minor=True)
        ax.set_xticks(arange(self.x_min,self.x_max,X_grad), major=True)

        ax.set_yticks(sorted(arange(0,min(Y),y_grad)+arange(y_grad,max(Y),y_grad)), minor=True)
        ax.set_yticks(sorted(arange(0,min(Y),y_grad)+arange(y_grad,max(Y),y_grad)), major=True)

        ax.grid(which='minor', linestyle='--', linewidth = 0.5, alpha=0.4)
        ax.grid(which='major', linewidth = 1, alpha=1)

        return(ax.plot(X,Y))

    

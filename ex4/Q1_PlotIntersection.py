from scipy.optimize import fsolve
from matplotlib import pyplot as plt
import numpy as np

def plotIntersection(x, f, g):
    """
    :param x: np.linespace - sequences of evenly spaced numbers
    :param f: first function
    :param g:second function
    :return:A plot of the functions with there intersections points using fsolve which finds the roots of a function.
    """
    ## findinig a range for all the relevant points
    x_th = [min(x), max(x)]
    y_th = [min(min(f(x)), min(g(x))), max(max(f(x)), max(g(x)))]

    ## creating a matrix for all the relevant points
    xv, yv = np.meshgrid(np.linspace(x_th[0], x_th[1], 21), np.linspace(y_th[0], y_th[1], 11))
    x0_grid = [(round(xx, 4), round(yy, 4)) for xx, yy in zip(xv.flatten(), yv.flatten())]

    roots = []
    for x0 in x0_grid:
        result = fsolve(lambda x: f(x) - g(x), x0=x0, xtol=0.00000001)  # xtol is a very smaal number- trashhold
        for rt in result:
            if np.isclose(f(rt), g(rt), rtol=1e-4):  ## if the point is close enough it means its a intersection point so add him to the roots
                roots.append(rt)
    roots = np.array(roots) # for plotting
    plt.plot(x, f(x), x, g(x), roots, f(roots), 'ro')
    plt.show()

if __name__ == '__main__':

    #-------------Let's define some functions---------------------
    f1 = lambda x : x**2
    g1 = lambda x : x+10
    f2 = lambda x : np.sin(x)
    g2 = lambda x : 0.2*x
    f3 = lambda x : x**3 + 4
    g3 = lambda x: np.cos(x)
    g4 = lambda x: x
    f4 = lambda x : x**2 + 2*x +4
    f5 = lambda x : 8*x +4
    f6 = lambda x : x +5
    f7 = lambda x : x+7
    g5 = lambda x: x**2
    g6 = lambda x: x+5
    g7 = lambda x: x**2 +7*x +1
    f8 = lambda x : x**2
    f9 = lambda x : -0.5*x +7
    f10 = lambda x : -x
    g10 = lambda x: x
    g9 = lambda x: 2*x +3
    g8 = lambda x: x**0.5

#----------------- Lest's plot the  intersection points of some functions ---------------------
    plotIntersection(np.linspace(-10, 10, 1000), f1, g1)
    plotIntersection(np.linspace(-10, 10, 1000), f2, g2)
    plotIntersection(np.linspace(-10, 10, 1000), f3, g3)
    plotIntersection(np.linspace(-10, 10, 1000), f4, g4) ## there is no intersection
    plotIntersection(np.linspace(-10, 10, 1000), f5, g5)
    plotIntersection(np.linspace(-10, 10, 1000), f6, g6) ## same function - many points
    plotIntersection(np.linspace(-10, 10, 1000), f7, g7)
    plotIntersection(np.linspace(-10, 10, 1000), f8, g8)
    plotIntersection(np.linspace(-10, 10, 1000), f9, g9)
    plotIntersection(np.linspace(-10, 10, 1000), f10, g10)












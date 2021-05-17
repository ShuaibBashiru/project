import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
from scipy.optimize import brentq
import matplotlib.pyplot as plt
from django.http import JsonResponse, HttpResponse
from pyswarms.utils.search import RandomSearch
from scipy.optimize import minimize_scalar
from sympy import symbols, solve, Eq

def testing():
    x = symbols('x')
    equation = Eq(-x ** 2 + 5 * x ** 2 + 20, 0)
    sol = solve(equation)
    print(sol[0])

# testing()


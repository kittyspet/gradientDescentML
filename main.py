import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy import cos, sin, pi, E, exp
import time


def build_graf(_fig, line, column, index, title, _x, _y, _z):
        ax = _fig.add_subplot(line, column, index, projection='3d')
        ax.plot_surface(_x, _y, _z, alpha=0.25)
        ax.title.set_text(title)
        # ax.set_xlim((-15, 15))
        # ax.set_ylim((-15, 15))
        # ax.set_zlim((-15, 15))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        return ax


# Функция Экли
def f1(_x, _y):
    return (- 20 * np.exp(- 0.2 * np.sqrt(0.5 * (_x ** 2 + _y ** 2))) -
            np.exp(0.5 * (np.cos(2 * np.pi * _x) + np.cos(2 * np.pi * _y))) + np.e + 20)


def df1dx(_x, _y):
    return (2.8284 * _x * np.exp(-0.1414 * np.sqrt(_x ** 2 + _y ** 2))) / (np.sqrt(_x ** 2 + _y ** 2)) + np.pi * np.exp(
            0.5 * np.cos(2 * np.pi * _x) + 0.5 * np.cos(2 * np.pi * _y)) * np.sin(2 * np.pi * _x)


def df1dy(_x, _y):
    return (2.8284 * _y * np.exp(-0.1414 * np.sqrt(_x ** 2 + _y ** 2))) / (np.sqrt(_x ** 2 + _y ** 2)) + np.pi * np.exp(
            0.5 * np.cos(2 * np.pi * _x) + 0.5 * np.cos(2 * np.pi * _y)) * np.sin(2 * np.pi * _y)


# Функция Бута
def f2(_x, _y):
    return (_x + 2 * _y - 7) ** 2 + (2 * _x + _y - 5) ** 2


def df2dx(_x, _y):
    return 10 * _x + 8 * _y - 34


def df2dy(_x, _y):
    return 8 * _x + 10 * _y - 38


import numpy as np
import pyvista as pv

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    
)

from sympy import Symbol, symbols, solve, Eq
import sympy
from sympy.parsing.latex import parse_latex

class Window(QMainWindow):

    def __init__(self):
        main = QWidget()
        self.setCentralWidget(main)

        layout = QHBoxLayout()
        main.setLayout(layout) 

        nav = QWidget()
        nav_layout = QVBoxLayout()
        nav.setLayout(nav_layout)

        nav.addWidget(QLabel("Enter formula (or copy from desmos)"))
        nav.addWidget(QLineEdit("2x+y=5"))

def subConstants(latex):
    return latex.subs(Symbol("e"), sympy.E).subs(Symbol("pi"), sympy.pi)

def solveLatex(latex: str, input, solve_for: str):

    solver = Eq(subConstants(parse_latex(latex.split("=")[0])), subConstants(parse_latex(latex.split("=")[1])))

    symbs = {}
    if solve_for == "y":
        symbs["x"] = input
    if solve_for == "x":
        symbs["y"] = input


    subbed = solver.subs(symbs)

    sol = solve(subbed, symbols(solve_for))

    evaluated = [x.evalf() for x in sol]

    return evaluated

print(solveLatex("e+3=y", -2, "y"))

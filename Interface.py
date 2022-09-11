# -*- coding: utf-8 -*-
"""

"""

import PySimpleGUI as sg
import sympy as sym
from math import sqrt
from math import e
import numpy as np
import sympy.parsing.sympy_parser as symp
from sympy.parsing.sympy_parser import parse_expr
from numpy.linalg import inv

transformations = (symp.standard_transformations +(symp.implicit_multiplication_application,))


sg.theme('LightGreen4')  # please make your windows colorful

layout = [[sg.InputCombo(('Busquedas incrementales', 'Biseccion','Regla falsa','Punto fijo',
                          'Secante','Newton','Raices multiples','Jacobi','Factorización LU','GaussSeidel','Eliminación Gaussiana',
                          'Pivoteo parcial','Pivoteo total','Diferencias divididas',
                          'Interpolación Lagrange','Splines cuadráticas')
                         , size=(30, 1))],
            [sg.Submit(), sg.Cancel()]]

window = sg.Window('Escoger método', layout)

event, values = window.read()
window.close()
metodo =  values[0]

def entradaMatricesAb(n):
    col1 = [[sg.Text('A')],
           [sg.Input()],
           [sg.Text('b')],
           [sg.Input()]]
    col2 = [[sg.Text('A')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()]]
    col3 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col4 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col5 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col6 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col7 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col8 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col9 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    col10 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Text('b')],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()],
           [sg.Input()]]
    
    if n==1:
        col=col1
    elif n==2:
        col=col2
    elif n==3:
        col = col3
    elif n==4:
        col = col4
    elif n==5:
        col = col5
    elif n==6:
        col = col6
    elif n==7:
        col = col7
    elif n==8:
        col = col8
    elif n==9:
        col = col9
    elif n==10:
        col = col10
        
    return col

def entradaMatricesA(n):
    col1 = [[sg.Text('A')],
           [sg.Input()]]
    col2 = [[sg.Text('A')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col3 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input()]]
    col4 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    col5 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    col6 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    col7 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    col8 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    col9 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    col10 = [[sg.Text('A')],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()],
           [sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input(),sg.Input()]]
    
    if n==1:
        col=col1
    elif n==2:
        col=col2
    elif n==3:
        col = col3
    elif n==4:
        col = col4
    elif n==5:
        col = col5
    elif n==6:
        col = col6
    elif n==7:
        col = col7
    elif n==8:
        col = col8
    elif n==9:
        col = col9
    elif n==10:
        col = col10
        
    return col

def entradaPuntos(n):
    col1 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()]]
    
    col2 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    
    col3 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    
    col4 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col5 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col6 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col7 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col8 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col9 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    col10 = [[sg.Text('x'),sg.Text('y')],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()],
           [sg.Input(),sg.Input()]]
    if n==1:
        col=col1
    elif n==2:
        col =col2
    elif n==3:
        col =col3
    elif n==4:
        col =col4
    elif n==5:
        col =col5
    elif n==6:
        col =col6
    elif n==7:
        col =col7
    elif n==8:
        col =col8
    elif n==9:
        col =col9
    elif n==10:
        col =col10
        
    return col

def busquedasIncrementales (f, x0, deltax, numIteracion):
  if f.subs(x, x0) == 0:
    return (str(x0) + " Es una raíz de " + str(f))
  else: 
    xn = x0 + deltax
    iter = 0
  while (numIteracion > iter and (f.subs(x,x0) * f.subs(x,xn)) > 0):
    x0 = xn
    xn = x0 + deltax
    iter += 1
  if f.subs(x,xn) == 0:
    return (str(xn) + " Es una raíz de " + str(f))
  elif (f.subs(x,x0) * f.subs(x,xn)) < 0:
    return ("Existe una raíz de " + str(f) + " entre " + str(x0) + " y " + str(xn))
  else:
    return ("No se han encontrado raices")
    
x = sym.Symbol('x')
    

if metodo =='Busquedas incrementales':
    sg.theme('LightYellow')  # please make your windows colorful

    layout = [[sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
            [sg.Text('deltax', size=(15, 1)), sg.InputText()],
            [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Busquedas incrementales', layout)

    event, values = window.read()
    window.close()
    f,x0, deltax, numIteracion = values[0],float(values[1]), float(values[2]),int(values[3]) 
    
    f = parse_expr(f, transformations=transformations)
    
    sg.Popup('Resultados de busquedas incrementales',
             busquedasIncrementales (f, x0, deltax, numIteracion))
    window.close()
    
def biseccion(f,xi, xf, tol, numIter):
  if (f.subs(x,xi) * f.subs(x,xf) == 0):
    if (f.subs(x,xi) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xi))
    if (f.subs(x,xf) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xf))
  elif (f.subs(x,xi) * f.subs(x,xf) > 0):
    return("No se encuentran raices de " + str(f) )
  else: 
    xm = (xi + xf)/2
    numIteracion = 0
    error = abs(xi-xm)
    while (error>tol and numIteracion<numIter and f.subs(x,xm) != 0):
      if (f.subs(x,xi) * f.subs(x,xm) < 0):
        xf = xm
      else: 
        xi = xm
      xm = (xi + xf) / 2
      error = abs(xm - xi)
      numIteracion += 1
    if (f.subs(x,xm) == 0):
      return("Se halló una raíz en " + str(xm) )
    elif error < tol: 
      return( str(xm) + " es raíz, con una toleracia de " + str(tol))
    else:
      return("No se halló una solución")
     
if metodo =='Biseccion':
    sg.theme('Light Purple')  # please make your windows colorful

    layout = [[sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('xinicial', size=(15, 1)), sg.InputText()],
              [sg.Text('xfinal', size=(15, 1)), sg.InputText()],
            [sg.Text('tolerancia', size=(15, 1)), sg.InputText()],
            [sg.Text('Numerodeiteraciones', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Bisección', layout)

    event, values = window.read()
    window.close()
    f,x0, xf, tol, numIter = values[0], float(values[1]),float(values[2]),float(values[3]),int(values[4]) 
    
    f = parse_expr(f, transformations=transformations)
    
    sg.Popup('Resultados de bisección',
             biseccion(f,x0, xf, tol, numIter))
    window.close()
    
def reglaFalsa (f,xi, xf, tol, numIter):
  if (f.subs(x,xi) * f.subs(x,xf) == 0):
    if (f.subs(x,xi) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xi))
    if (f.subs(x,xf) == 0):
      return("Hay una raíz de " + str(f) + " en " + str(xf))
  elif (f.subs(x,xi) * f.subs(x,xf) > 0):
    return("No se encuentran raices de " + str(f) )
  else: 
    xm = xf -((f.subs(x,xf)*(xi-xf))/(f.subs(x,xi)-f.subs(x,xf)))
    xm = float(xm)
    numIteracion = 0
    error = abs(xi-xm)
    while (error>tol and numIteracion<numIter and f.subs(x,xm) != 0):
      if (f.subs(x,xi) * f.subs(x,xm) < 0):
        xf = xm
      else: 
        xi = xm
      xm = xf -((f.subs(x,xf)*(xi-xf))/(f.subs(x,xi)-f.subs(x,xf)))
      xm = float(xm)
      error = abs(xm - xf)
      numIteracion += 1
    if (f.subs(x,xm) == 0):
      return("Se halló una raíz en " + str(xm) )
    elif error < tol: 
      return( str(xm) + " es raíz con una toleracia de " + str(tol))
    else:
      return("No se halló una solución")
     
if metodo =='Regla falsa':
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
            [sg.Text('xf', size=(15, 1)), sg.InputText()],
            [sg.Text('tol', size=(15, 1)), sg.InputText()],
            [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Regla falsa', layout)

    event, values = window.read()
    window.close()
    f,x0, xf,tol, numIter = values[0],float(values[1]), float(values[2]),float(values[3]),int(values[4]) 
    f = parse_expr(f, transformations=transformations)
    
    sg.Popup('Resultados de regla falsa',
             reglaFalsa (f,x0, xf, tol, numIter))
    window.close()
     
def puntoFijo(f,x0,numIter, tol):
  g= -(f-x)
  iter = 0
  error = tol + 1
  while (iter < numIter and error > tol):
    xn = float(g.subs(x,x0))
    error = abs(xn - x0)
    iter += 1
    x0 = xn
  if error <= tol:
    return(str(xn) + " es raíz con tolerancia de " + str(tol))
  else:
    return("El método no converge")
    
    
if metodo =='Punto fijo':
    sg.theme('LightBlue1')  # please make your windows colorful

    layout = [[sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
            [sg.Text('tol', size=(15, 1)), sg.InputText()],
            [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Regla falsa', layout)

    event, values = window.read()
    window.close()
    f,x0,tol, numIter = values[0],float(values[1]), float(values[2]),int(values[3]) 
    f = parse_expr(f, transformations=transformations)
    
    sg.Popup('Resultados de punto fijo',
             puntoFijo(f,x0, numIter,tol))
    window.close()
    
def metodoSecante(f,x0,x1,numIter,tol):
  iter = 0
  while iter <= numIter:
    newX1 = float(x1 - (f.subs(x, x1)*((x1 - x0) / (f.subs(x, x1) - f.subs(x, x0)))))
    if f.subs(x, x0) == 0:
      return(str(x0) + " es una raíz de " + str(f))
    elif abs(newX1 - x1) <= tol:
      return(str(newX1) + " es raíz con tolerancia " + str(tol) + " con "+ str(iter)+" iteraciones."  )
    elif iter > numIter:
      return("El metodo no converge en estas iteraciones " + str(iter))
    else:
      iter += 1
      x0 = x1
      x1 = newX1

if metodo =='Secante':
    sg.theme('BluePurple')  # please make your windows colorful

    layout = [[sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
            [sg.Text('xf', size=(15, 1)), sg.InputText()],
            [sg.Text('tol', size=(15, 1)), sg.InputText()],
            [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Secante', layout)

    event, values = window.read()
    window.close()
    f,x0, xf,tol, numIter = values[0],float(values[1]), float(values[2]),float(values[3]),int(values[4]) 
    f = parse_expr(f, transformations=transformations)
    
    
    sg.Popup('Resultados Secante',
             metodoSecante(f,x0,xf,numIter,tol))
    window.close()
      
def Newton (f, df, x0, numIter, tol):
  cont = 0
  error = tol + 1
  while (cont < numIter and error > tol):
    xn = x0 - float(f.subs(x, x0))/float(df.subs(x, x0))
    error = abs(xn - x0)
    cont += 1
    x0 = xn
  if error <= tol:
    return(str(xn) + " es raíz con tolerancia " + str(tol)+ " y el algorítmo paró en la iteración: " + str(cont))
  else:
    return("El método no converge")

if metodo =='Newton':
    sg.theme('BluePurple')  # please make your windows colorful

    layout = [[sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
            [sg.Text('tol', size=(15, 1)), sg.InputText()],
            [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Newton', layout)

    event, values = window.read()
    window.close()
    f,x0, tol,numIter = values[0],float(values[1]), float(values[2]),int(values[3]) 
    
    f = parse_expr(f, transformations=transformations)
    df = sym.diff(f, x)
    
    sg.Popup('Resultados Newton',
             Newton (f, df, x0, numIter, tol))
    window.close()
    
def RaicesMultiples (f, df, dff, x0, numIter, tol):
  iter = 0
  error = tol + 1
  while (iter < numIter and error > tol):
    xn = x0 - (float(f.subs(x, x0)*df.subs(x,x0))/float(df.subs(x, x0)**2-(f.subs(x, x0)*dff.subs(x,x0))))
    error = abs(xn - x0)
    iter += 1
    x0 = xn
  if error <= tol:
    return(str(xn) + " es raíz con tolerancia " + str(tol))
  else:
    return("El método no converge")

if metodo =='Raices multiples':
    sg.theme('LightYellow')  # please make your windows colorful

    layout = [[sg.Text('f', size=(15, 1)), sg.InputText()],
              [sg.Text('x0', size=(15, 1)), sg.InputText()],
            [sg.Text('tol', size=(15, 1)), sg.InputText()],
            [sg.Text('numIteracion', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Raíces multiples', layout)

    event, values = window.read()
    window.close()
    f,x0, tol,numIter = values[0],float(values[1]), float(values[2]),int(values[3]) 
    
    f = parse_expr(f, transformations=transformations)
    df = sym.diff(f, x)
    dff= sym.diff(df,x)
    
    sg.Popup('Raíces multiples',
             RaicesMultiples (f, df, dff, x0, numIter, tol))
    window.close()
    
def factorizacionLU(A):
    n, m = A.shape
    P = np.identity(n)
    L = np.identity(n)
    U = A.copy()
    PF = np.identity(n)
    LF = np.zeros((n,n))
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:,k]))
        index = index + k 
        if index != k:
            P = np.identity(n)
            P[[index,k],k:n] = P[[k,index],k:n]
            U[[index,k],k:n] = U[[k,index],k:n] 
            PF = np.dot(P,PF)
            LF = np.dot(P,LF)
        L = np.identity(n)
        for j in range(k+1,n):
            L[j,k] = -(U[j,k] / U[k,k])
            LF[j,k] = (U[j,k] / U[k,k])
        U = np.dot(L,U)
    np.fill_diagonal(LF, 1)
    return  LF, U



if metodo =='Factorización LU':
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Jacobi', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')

    col = entradaMatricesA(n)
        
    layout = [[sg.Column(col)],
              [sg.OK()]]
    
    window = sg.Window('FactorizacionLU', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
    
    A = []

    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    
    L,U=factorizacionLU(A)
        
    sg.Popup('FactorizacionLU',
             'La matriz L es: ',L,
             'La matriz U es: ',U)
    window.close()

def jacobi(A,b,tol,numIter):
  n = np.size(A,0)
  L = - np.tril(A, -1)
  U = - np.triu(A,1)
  D = A+L+U
  x0 = np.zeros([n,1])
  Tj = np.matmul(inv(D),(L+U))
  autovalores, autovectores = np.linalg.eig(Tj)
  autovalores = abs(autovalores)

  for lam in autovalores:
    if lam >= 1:
      return ("El método no converge.")

  C = np.matmul(inv(D),b)
  xn = (np.matmul(Tj,x0))+C
  error = np.array(abs(xn - (np.dot(Tj,xn)+C)))
  error = np.amax(error)
  iter = 0
  while ((error > tol) and (iter<numIter)):
    nuevo = np.matmul(Tj,xn)+C
    error = np.array(abs(nuevo-xn))
    error = np.amax(error)
    xn = nuevo
    iter = iter +1
  return("El método converge en "+str(xn))

if metodo =='Jacobi':
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Jacobi', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')

    col = entradaMatricesAb(n)
        
    layout = [[sg.Column(col)],
              [sg.Text('Tolerancia', size=(15, 1)), sg.InputText()],
              [sg.Text('NumeroIteraciones', size=(15, 1)), sg.InputText()],
              
              [sg.OK()]]
    window = sg.Window('Jacobi', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
    tol = values[cont]
    numIter = int(values[cont+1])
        
    sg.Popup('Jacobi',
             jacobi(A, b,tol,numIter))
    window.close()
    
def GaussSeidel(A,b,tol,numIter):
  n = np.size(A,0)
  L = - np.tril(A, -1)
  U = - np.triu(A,1)
  D = A+L+U
  x0 = np.zeros([n,1])
  Tg = np.matmul(inv(D-L),U)
  autovalores, autovectores = np.linalg.eig(Tg)
  autovalores = abs(autovalores)

  for lam in autovalores:
    if lam >= 1:
      return ("El método no converge.")

  C = np.matmul(inv(D-L),b)
  xn = (np.matmul(Tg,x0))+C
  error = np.array(abs(xn - (np.dot(Tg,xn)+C)))
  error = np.amax(error)
  iter = 0
  while ((error > tol) and (iter<numIter)):
    nuevo = np.matmul(Tg,xn)+C
    error = np.array(abs(nuevo-xn))
    error = np.amax(error)
    xn = nuevo
    iter = iter +1
  return("El método converge en "+str(xn))

if metodo =='GaussSeidel':
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('GaussSeidel', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Column(col)],
              [sg.Text('Tolerancia', size=(15, 1)), sg.InputText()],
              [sg.Text('NumeroIteraciones', size=(15, 1)), sg.InputText()],
              
              [sg.OK()]]
    window = sg.Window('GaussSeidel', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
    tol = values[cont]
    numIter = int(values[cont+1])
        
    sg.Popup('GaussSeidel',
             GaussSeidel(A, b,tol,numIter))
    window.close() 

def eliminacionGaussiana(A, b):
  n = b.size
  Ab =  np.append(A,b, axis=1)
  for k in range(n):
    for i in range(k+1,n):
      mult = Ab[i][k] / Ab[k][k]
      for j in range(k,n+1):
        Ab[i][j]=Ab[i][j]-mult*Ab[k][j]
  x = np.zeros(n)
  x[n-1]=Ab[n-1][n]/Ab[n-1][n-1]
  for i in range(n-1,-1,-1):
    sum= 0 
    for p in range(i+1,n):
      sum = sum + Ab[i][p] * x[p]
    x[i] = (Ab[i][n]-sum)/Ab[i][i]
  return x
    
if metodo =='Eliminación Gaussiana':
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Eliminación Gaussiana', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Column(col)],
              [sg.OK()]]
    window = sg.Window('Eliminación Gaussiana', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
        
    sg.Popup('Eliminación Gaussiana',
             eliminacionGaussiana(A, b))
    window.close()
    
    
def pivoteoParcial(A, b):
  n = b.size
  Ab =  np.append(A,b, axis=1)
  for k in range(n):
    c = max(abs(Ab[k:,k]))
    index = list(abs(Ab[:,k])).index(c)
    maxx = np.array(Ab[index,:],dtype=float)
    Ab[index,:] = np.array(Ab[k,:],dtype=float)
    Ab[k,:] = maxx
    Ab = np.array(Ab,dtype=float)
    for i in range(k+1,n):
      mult = Ab[i][k] / Ab[k][k]
      for j in range(k,n+1):
        Ab[i][j]=Ab[i][j]-mult*Ab[k][j]
  x = np.zeros(n)
  x[n-1]=Ab[n-1][n]/Ab[n-1][n-1]
  for i in range(n-1,-1,-1):
    sum= 0 
    for p in range(i+1,n):
      sum = sum + Ab[i][p] * x[p]
    x[i] = (Ab[i][n]-sum)/Ab[i][i]
  return x


if metodo =='Pivoteo parcial':
    sg.theme('Material1')
    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Pivoteo parcial', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Column(col)],
              [sg.OK()]]
    window = sg.Window('Pivoteo parcial', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
        
    sg.Popup('Pivoteo parcial',
             'Se obtiene como respuesta el vector x :',
             pivoteoParcial(A, b))
    window.close()
    
def pivoteoTotal(A, b):
  n = b.size
  Ab =  np.append(A,b, axis=1)
  Ab = np.array(Ab,dtype=float)
  x = np.array(list(range(n)))
  for k in range(0,n):
    A = Ab[:,:-1]
    c = abs(A[k:,k:]).max()
    index = np.where(abs(A)==c)

    c_temp = Ab[:,index[1][0]].copy()
    Ab[:,index[1][0]]= Ab[:,k].copy()
    Ab[:,k] = c_temp

    x_temp= x[index[1][0]]
    x[index[1][0]]= x[k]
    x[k]= x_temp

    r_temp= Ab[index[0][0],:].copy()
    Ab[index[0][0],:]= Ab[k,:].copy()
    Ab[k,:] = r_temp

    Ab[k,:]= Ab[k,:]*(1/c)

    for i in range(0,n):
      if i != k:
        Ab[i,:]= Ab[i,:].copy()+Ab[k,:].copy()*(-Ab[i,k].copy())

  S= Ab[:,-1]
  B=[]
  for i in range(0,n):
    B.append(float(S[np.where(x==i)]))
  return B

if metodo =='Pivoteo total':
    sg.theme('DarkRed')
    layout = [[sg.Text('Escoger el número de ecuaciones')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Pivoteo total', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])

    window = sg.Window('Columns')
    
    col = entradaMatricesAb(n)
        
    layout = [[sg.Column(col)],
              [sg.OK()]]
    window = sg.Window('Pivoteo total', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
        
    A = []
    b = []
    cont = 0
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont = cont +1
        A.append(row)
    A=np.array(A)
    for i in range(n):
        b.append([values[cont]])
        cont = cont+1
    b = np.array(b)
    
    sg.Popup('Pivoteo total',
             'Se obtiene como respuesta el vector x :',
             pivoteoTotal(A, b))
    window.close()
    
def diferenciasDivididas (puntos):
  n = np.size(puntos,0)
  X = puntos[:,0]
  Y = puntos[:,1]
  p = 0
  tabla = np.zeros([n, n])
  tabla[:,0] = Y
  for j in range(1,n):
    for i in range(n-j):
      tabla[i][j] = (tabla[i+1][j-1] - tabla[i][j-1]) / (X[i+j]-X[i])
  b = np.array(tabla[0,:])
  mult = 1
  for i in range(n):
    mult =1
    for j in range(i):
      mult = mult * (x-X[j])
    p = p + b[i]*(mult)
  p = sym.simplify(sym.expand(p))
  return ("El polinomio interpolante es: " +str(p))

if metodo =='Diferencias divididas':
    sg.theme('LightBlue5')
    
    layout = [[sg.Text('Escoger el número de puntos a interpolar')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Diferencias divididas', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])
    
    window = sg.Window('Columns')                                   # blank window

    col = entradaPuntos(n)
    
    layout = [[sg.Column(col)],
              [sg.OK()]]
    window = sg.Window('Diferencias divididas', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
    
    puntos = []
    
    cont = 0 
    for i in range(n):
        xy= [values[cont],values[cont+1]]
        puntos.append(xy)
        cont = cont+2
        
    puntos = np.array(puntos)
    
    sg.Popup('Diferencias divididas',
             diferenciasDivididas (puntos))
    window.close()
    
    
def lagrange(puntos):
  n = np.size(puntos,0)
  p = 0
  X = puntos[:,0]
  Y = puntos[:,1]
  for k in range(n):
    L=1
    for i in range(n):
      if i != k:
        L = L*((x-X[i])/(X[k]-X[i]))
    p = p +L*(Y[k])
  p = sym.simplify(sym.expand(p))
  return p
    
    
if metodo =='Interpolación Lagrange':
    sg.theme('LightBrown5')
    
    layout = [[sg.Text('Escoger el número de puntos a interpolar')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Polinomio interpolante de Lagrange', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])
    
    window = sg.Window('Columns')                                   # blank window

    col = entradaPuntos(n)
    
    layout = [[sg.Column(col)],
              [sg.OK()]]
    window = sg.Window('Polinomio interpolante de Lagrange', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
    
    puntos = []
    
    cont = 0 
    for i in range(n):
        xy= [values[cont],values[cont+1]]
        puntos.append(xy)
        cont = cont+2
        
    puntos = np.array(puntos)
        
    sg.Popup('Polinomio interpolante de Lagrange',
             lagrange(puntos))
    window.close()
    
    
def splinesCuadraticos(puntos):
  n = np.size(puntos,0)
  X = puntos[:,0]
  Y = puntos[:,1]
  y = [(Y[i//2]if i%2==0 else Y[(i)//2]) if i <= 2*(n-1) else 0 for i in range(1, 3*(n-1) + 1)]
  
  tabla = np.zeros([3*(n-1),3*(n-1)])

  for i in range(n-1):
    tabla[2*(i + 1) - 2][3*i] = tabla[2*(i + 1) - 1][3*i] = 1 
    tabla[2*(i + 1) - 2][3*i + 1] = X[i]
    tabla[2*(i + 1) - 2][3*i + 2] = X[i]**2
    tabla[2*(i + 1) - 1][3*i + 1] = X[i + 1]
    tabla[2*(i + 1) - 1][3*i + 2] = X[i + 1]**2

  for i in range(n-2):
    tabla[2*(n-1) + i][3*i + 1] = 1
    tabla[2*(n-1) + i][3*i + 4] = -1 
    tabla[2*(n-1) + i][3*i + 2] = 2*X[i + 1]
    tabla[2*(n-1) + i][3*i + 5] = -2*X[i + 1]

  tabla[3*(n-1) - 1][2] = 2

  tabla = np.linalg.inv(tabla)
  coef = np.matmul(tabla,y)
  p=[]
  cont = 0
  for j in range(n-1):
    pj = coef[cont] + coef[cont+1] * x + coef[cont+2]*x**2
    cont=cont+3
    p.append(pj)
  return p
    
    
if metodo =='Splines cuadráticas':
    sg.theme('BlueMono')
    
    layout = [[sg.Text('Escoger el número de puntos a interpolar')],
              [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=3)],
            [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Splines cuadráticas', layout)

    event, values = window.read()
    window.close()
    
    n = int(values[0])
    
    window = sg.Window('Columns')                                   # blank window

    col = entradaPuntos(n)
    
    layout = [[sg.Column(col)],
              [sg.OK()]]
    window = sg.Window('Splines cuadráticas', layout)

    event, values = window.read()
    window.close()
    
    for i in range(len(values)):
        values[i]=float(values[i])
    
    puntos = []
    
    cont = 0 
    for i in range(n):
        xy= [values[cont],values[cont+1]]
        puntos.append(xy)
        cont = cont+2
        
    puntos = np.array(puntos)
    
    sg.Popup('Splines cuadráticas',
             'Los polinomios interpolantes son los siguientes: ',
             splinesCuadraticos(puntos))
    window.close()
    
    

    






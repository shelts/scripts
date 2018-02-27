#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Hessian matrix implementation for calculating error in fits             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import numpy as np
from numpy.linalg import inv


def function(p):
    x = p[0]
    y = p[1]
    z = p[2]
    
    f = x * y * z + x**2 * y * z + x * y**2 * z + x * y * z**2
    return f

class hessian:
    def __init__(self, cost, parameters):
        self.cost = cost
        self.paras = parameters
        #self.paras = [2.0, 3.0, 4.0]
        self.dim = len(self.paras)
        self.create_matrix()
        self.invert()
        
    def create_matrix(self):
        self.H = []
        for i in range(0, self.dim):
            self.H.append([])
            for j in range(0, self.dim):
                derivative = self.calc_derivative(i, j)
                self.H[i].append(derivative)
            print self.H[i]
       
       
    def calc_derivative(self, i, j):
        h1 = 0.00001
        h2 = 0.00001
        
        a = self.paras[i]
        b = self.paras[j]
        p = self.paras
        if(i == j): # straight up second derivative
            f1 = function(p)
            f1 = self.cost.get_cost(p)
            
            p[i] = a + h1
            f2 = function(p)
            f2 = self.cost.get_cost(p)
            
            p[i] = a - h1
            f3 = function(p)
            f3 = self.cost.get_cost(p)
            
            der = f2 - 2.0 * f1 + f3
            der = der / (h1 * h1)
            
        else: # second partial derivative
            p[i] = a + h1
            p[j] = b + h2
            f1 = function(p)
            f1 = self.cost.get_cost(p)
        
            p[i] = a + h1
            p[j] = b - h2
            f2 = function(p)
            f2 = self.cost.get_cost(p)
            
            p[i] = a - h1
            p[j] = b + h2
            f3 = function(p)
            f3 = self.cost.get_cost(p)
            
            p[i] = a - h1
            p[j] = b - h2
            f4 = function(p)
            f4 = self.cost.get_cost(p)
            
            der = f1 - f2 - f3 + f4
            
            der = der / (4.0 * h1 * h2)
        
        return der
        
    def invert(self):
        self.diags = []
        array = []
        for i in range(0, self.dim):
            array.append(self.H[i])
        a = np.array(array)
        a_inv = inv(a)
        for i in range(0, self.dim):
            self.diags.append(a_inv[i][i])
        print a_inv
#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Hessian matrix implementation for calculating error in fits             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class hessian:
    def __init__(self, cost, parameters):
        self.cost = cost
        self.paras = parameters
        self.dim = len(parameters)
        
        self.create_matrix()
        
    def create_matrix(self):
        self.H = []
        for i in range(0, self.dim):
            self.H.append([])
            for j in range(0, self.dim):
                derivative = self.calc_derivative(i, j)
                self.H[i].append(derivative)
            print self.H[i]
       
       
    def calc_derivative(self, i, j):
        h1 = 0.01
        h2 = 0.01
        
        a = self.paras[i]
        b = self.paras[j]
        p = self.paras
        
        p[i] = a + h1
        p[j] = b + h2
        f1 = self.cost.get_cost(p)
        
        p[i] = a + h1
        p[j] = b - h2
        f2 = self.cost.get_cost(p)
        
        
        p[i] = a - h1
        p[j] = b + h2
        f3 = self.cost.get_cost(p)
        
        p[i] = a - h1
        p[j] = b - h2
        f4 = self.cost.get_cost(p)
        
        der = f1 - f2 - f3 + f4
        der = der / (4.0 * h1 * h2)
        
        return der
        
        
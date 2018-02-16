#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Cost function for the data fitting                                      #
# You would need to change depending on the problem                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import math as mt

class cost_function: # function to get the cost associated with a parameter set
    def __init__(self, xs, ys):
        self.ys = ys
        self.xs = xs
        
    def least_square(self, function_values): # does a least square calculation. Not fitting function specific
        Rsq = 0.0
        for i in range(0, len(function_values)): 
            Rsq += (self.ys[i] - function_values[i])**2.0
            
        return Rsq**0.5
    
    def function(self, parameters, x_value):# this is the fitting function. Specific to the problem at hand
        m = parameters[0]
        b = parameters[1]
        
        A   = parameters[2]
        mu  = parameters[3]
        sig = parameters[4]
        
        #m2 = parameters[5]
        #b2 = parameters[6]
        
        linear = m * x_value + b # linear model to fit the background
        #linear2 = m2 * x_value + b
        guass = A * mt.exp( -(x_value - mu)**2.0 / (2.0 * sig**2.0)) # guass model to fit the on field 
        
        return linear + guass 
        
    def get_cost(self, parameters): #function to get the costs from a set of parameters
        function_values = []
        for i in range(0, len(self.xs)):
            function_values.append(self.function(parameters, self.xs[i])) # get the function values for each of the data's x values
        
        cost = self.least_square(function_values) # get the cost associated with the function values
        return cost
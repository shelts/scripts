#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Implementation of a Differential Evolution Optimization Algorithm.      #
# With reflective boudary conditions.                                     #
# Search ranges are for each parameter.                                   #
# This is generalized for the optimizer so you can add more parameters.   #
# You would need to change the cost class and test data class.            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import math as mt
import random
import matplotlib.pyplot as plt
from cost import *

#random.seed(a = 12345678)

#search_ranges = [ [-100.0, 100.0], # line slope a \
                  #[0.0, 100.0],    # y-inter b \
                  #[0.0, 300.0],    # guass amp A \
                  #[-4.0, 4.0],     # guass mu \
                  #[0.1, 10],        # guass sigma \
                #] 

search_ranges = [ [-100.0, 100.0], # line slope a \
                  [-10.0, 100.0],    # y-inter b \
                  [0.0, 10000.0],    # guass amp A \
                  [-4.0, 4.0],     # guass mu \
                  [0.01, 100],        # guass sigma \
                ]
                  #[-1000.0, 1000.0], # line slope a \
                  #[-1000.0, 1000.0],    # y-inter b \
                #] 


            
class population: # a class to create, store and update a population for differential evolution 
    def __init__(self, population_size, Nparameters):
        self.cur_pop = [] # to hold the entire population of parameters
        self.pop_costs = [] # the costs for each member of the population
        self.pop_size = population_size # size of the working population
        self.Nparas = Nparameters # the number of parameters that makes up each member of the population
        
        for i in range(0, population_size): # empty container for each member of the population
            self.cur_pop.append([])
        
    def initialize(self, ranges, cost): # function to initialize the population 
        for i in range(0, self.pop_size): # for every member of the population
            for j in range(0, self.Nparas): # for each parameter in each population member
                if(ranges[j].lower == ranges[j].upper):
                    val = ranges[j].lower
                else:
                    val = random.uniform(ranges[j].lower, ranges[j].upper) # get a random value within the search range for that parameter
                self.cur_pop[i].append(val) 
            cost_value = cost.get_cost(self.cur_pop[i]) # get cost for each member of the population
            self.pop_costs.append(cost_value)

                 
    def update(self, x, cross_over, differential_weight, cost, ranges): # function to update the population set using the diff evo algorithm
        a = -1 # to get them into the loop
        b = -1
        c = -1
        while(a == b or a == c or b == c or a == x or b == x or c == x): # pick unique agents
            a = int(random.uniform(0, self.pop_size))
            b = int(random.uniform(0, self.pop_size))
            c = int(random.uniform(0, self.pop_size))
        
        dimentionality = int(random.uniform(0, self.Nparas))#problem dimentionality, i.e. ranged between how many parameters we are fitting
        possible_new_set = [] 
        
        # create the possible new set of parameters:
        # uses the diff evolution aglorithm
        for i in range(0, self.Nparas):
            ri = random.uniform(0, 1)
            feasible = False # reset the feasibility
            if(ranges[i].lower == ranges[i].upper): # if the search range is fixed
                y = ranges[i].lower
            elif(ri < cross_over or i == dimentionality):
                y = self.cur_pop[a][i] + differential_weight * (self.cur_pop[b][i] - self.cur_pop[c][i])
            else:
                y = self.cur_pop[x][i]
                
            while(not feasible): #reflection boundary conditions
                if(y > ranges[i].upper): # above the upper boundary
                    y = 2.0 * ranges[i].upper - y # pull it back
                elif(y < ranges[i].lower): #below the lower boundary
                    y = 2.0 * ranges[i].lower - y # pull it back
                else:
                    feasible = True # if its good, send it through
            possible_new_set.append(y)
        
        # get the cost associated with this new set
        possible_new_cost = cost.get_cost(possible_new_set)
        
        if(possible_new_cost < self.pop_costs[x]): # if the new cost is better keep it. closer to zero is better.
            self.cur_pop[x] = possible_new_set # replace the current population member with the new set
            self.pop_costs[x] = possible_new_cost # replace the cost with the new
        return 0

class diff_evo: 
    class parameter: # quick class for the parameter search ranges
        def __init__(self, ranges):
            self.lower = ranges[0]
            self.upper = ranges[1]
                
    def __init__(self, xs, ys, iters):
        self.cross_over = 0.9 # algorithm specific parameter
        self.differential_weight = 0.8 # algorithm specific parameter
        self.pop_size = 10 * (len(search_ranges)) # size of the population
        self.Nparameters = len(search_ranges) # using the len of the search ranges as the number of parameters to keep it general
        self.optimization_iterations = iters  # number of iterations to run the optimization
        self.ranges = []
        
        for i in range(0, self.Nparameters): # setting up the search ranges
            val = self.parameter(search_ranges[i])
            self.ranges.append(val)
        
        self.cost = cost_function(xs, ys) #initialize cost function class with x and y values of the data
        
        # create the initial population: 
        self.pop = population(self.pop_size, self.Nparameters)# creates an empty population
        self.pop.initialize(self.ranges, self.cost)# gives random values to the parameters for each pop member and gets their cost
        
        self.run_optimization() # runs the optimization
        
    
    def get_bests(self): # finds the best cost in the population
        best_index = 0
        for i in range(1, self.pop_size):
            if(self.pop.pop_costs[i] < self.pop.pop_costs[best_index]): # check for the best cost
                best_index = i # just keep the best index. that maps to everything needed
        return best_index
    
    def run_optimization(self): # runs through the optimization. Each iteration updates the population
        counter = 0
        cost = self.pop.pop_costs[0]
        while(counter < self.optimization_iterations): # TODO: instead of running for a fixed number of iterations, should have a threshold on the cost
            # note: this updates the population as you go. does not create a new updated population list. 
            for i in range(0, self.pop_size): # will go through each member of the current population to update it
                self.pop.update(i, self.cross_over, self.differential_weight, self.cost, self.ranges) # this will update the member of the population
                counter += 1
            self.best_index = self.get_bests()
            
            #if(counter % 100 and (cost != self.pop.pop_costs[self.best_index]) ): # used for plotting the fits as it optimizes. not putting in if statement because not too needed or used.
                #self.plot_current_best(counter)
                #cost = self.pop.pop_costs[self.best_index]



    def generate_plot_points(self): # uses the fitting function with the best set of parameters to generate plottable points
        x = -6.0 #TODO: make the parameters here generalizable. right now these are hard coded to my problem
        dx = (6.0 - -6.0) / 100.0
        xs = []
        fs = []
        for i in range(0, 100): 
            f = self.cost.function(self.pop.cur_pop[self.best_index], x) # simple way of getting my function points out
            x += dx
            fs.append(f)
            xs.append(x)
            
        return xs, fs
            
    def plot_current_best(self, counter): # plots the current best parameter set. unique to this problem
        xs, fs = self.generate_plot_points()
        print self.pop.cur_pop[self.best_index], self.pop.pop_costs[self.best_index]
        plt.ylim(0, 100)
        plt.xlim(-6, 6)
        plt.plot(xs, fs, linewidth = 2, color = 'r')
        plt.scatter(self.cost.xs, self.cost.ys, s = 8, color = 'b', marker='o')
        plt.savefig('fitting/fit_' + str(counter) + '.png', format='png')
        plt.clf()
        

# main here is to be turned on when you want to test this algorithm. 
# It will create a test data set and then optimizate on it.
# can also be used to have it train on test data
#def main():
    #test = test_data()
    #test.plot()
    #diff_evo(test.xs, test.fsn)
#main()
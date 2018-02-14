#! /usr/bin/python

import math as mt
import random
import matplotlib.pyplot as plt
random.seed(a = 12345678)
search_ranges = [ [0.0, 10.],# line slope a \
                  [0.0, 100.0],   # y-inter b \
                  [0.0, 100.0],   # guass amp A \
                  [-2.0, 2.0],    # guass mu \
                  [0.1, 5]       # guass sigma \
                ] 
        #correct: 0.0, 25, 50, 0, 0.7

class test_data():
    def __init__(self):
        self.N = 30
        self.data_range = [-4.0,4.0]
        self.m = 0.0
        self.b = 25.0
        
        self.A = 50.0
        self.mu = 0
        self.sig = mt.sqrt(0.5)#0.7
        
        self.generate_points()
    def func(self, x):
        linear = self.m * x + self.b
        guass = self.A * mt.exp( -(x - self.mu)**2.0 / (2.0 * self.sig**2.0))
        return linear + guass
    
    def generate_points(self):
        self.fs = []
        self.xs = []
        x = self.data_range[0]
        dn = abs(self.data_range[0] - self.data_range[1]) / float(self.N)
        for i in range(0, self.N):
            x += dn
            f = self.func(x)
            self.xs.append(x)
            self.fs.append(f)
        
        self.guass_noise()
        
    def guass_noise(self):
        a = 2.0
        mu = 1.0
        sig = 2.0
        self.fsn = []
        for i in range(0, self.N):
            self.fsn.append(self.fs[i])
            x = random.uniform(-2, 2)
            noise = a * mt.exp( -(x - mu)**2.0 / (2.0 * sig**2.0))
            if(x > 0.0):
                self.fsn[i] += noise
            else:
                self.fsn[i] -= noise
        
    def plot(self):
        plt.ylim(0, 100)
        plt.xlim(-6, 6)
        plt.plot(self.xs, self.fs, linewidth = 2, color = 'r')
        plt.scatter(self.xs, self.fsn, s = 8, color = 'b', marker='o')
        plt.savefig('quick_plots/test_data.png', format='png')

        
class population: # a class to create, store and update a population for differential evolution 
    def __init__(self, population_size, Nparameters):
        self.cur_pop = []
        self.pop_costs = []
        self.size = population_size
        self.Nparas = Nparameters
        for i in range(0, population_size):
            self.cur_pop.append([])
        
    def initialize(self, ranges, cost):
        for i in range(0, self.size):
            for j in range(0, self.Nparas):
                val = random.uniform(ranges[j].lower, ranges[j].upper)
                self.cur_pop[i].append(val)
            cost_value = cost.get_cost(self.cur_pop[i])
            self.pop_costs.append(cost_value)

                 
    def update(self, x, cross_over, differential_weight, cost): 
        a = -1
        b = -1
        c = -1
        while(a == b or a == c or b == c or a == x or b == x or c == x): # pick unique agents
            a = int(random.uniform(0, self.size))
            b = int(random.uniform(0, self.size))
            c = int(random.uniform(0, self.size))
        #print a, b, c, x
        dimentionality = int(random.uniform(0, self.Nparas))#problem dimentionality
        possible_new_set = []
        
        # create the possible new set of parameters:
        for i in range(0, self.Nparas):
            ri = random.uniform(0, 1)
            if(ri < cross_over or i == dimentionality):
                y = self.cur_pop[a][i] + differential_weight * (self.cur_pop[b][i] - self.cur_pop[c][i])
                possible_new_set.append(y)
            else:
                y = self.cur_pop[x][i]
                possible_new_set.append(y)
        
        # get the cost associated with this new set
        possible_new_cost = cost.get_cost(possible_new_set)
        #print possible_new_cost, self.pop_costs[x]
        if(possible_new_cost < self.pop_costs[x]):# if the new cost is better keep it
            #print 'this ran'
            self.cur_pop[x] = possible_new_set
            self.pop_costs[x] = possible_new_cost
        return 0
    
class cost_function:
    def __init__(self, ys, xs):
        self.ys = ys
        self.xs = xs
        
    def least_square(self, function_values):
        Rsq = 0.0
        for i in range(0, len(function_values)):
            Rsq += (self.ys[i] - function_values[i])**2.0
            
        return Rsq**0.5
    
    def function(self, parameters, x_value):
        m = parameters[0]
        b = parameters[1]
        
        A   = parameters[2]
        mu  = parameters[3]
        sig = parameters[4]
        
        linear = m * x_value + b
        guass = A * mt.exp( -(x_value - mu)**2.0 / (2.0 * sig**2.0))
        
        return linear + guass
        
    def get_cost(self, parameters):
        function_values = []
        for i in range(0, len(self.xs)):
            function_values.append(self.function(parameters, self.xs[i]))
        
        cost = self.least_square(function_values)
        return cost
    
class diff_evo:
    class parameter:
        def __init__(self, ranges):
            self.lower = ranges[0]
            self.upper = ranges[1]
                
    def __init__(self, ys, xs):
        self.cross_over = 0.9
        self.differential_weight = 0.8
        self.pop_size = 50
        self.Nparameters = len(search_ranges)
        #self.best_index
        self.ranges = []
        
        for i in range(0, self.Nparameters):
            val = self.parameter(search_ranges[i])
            self.ranges.append(val)
        
        self.cost = cost_function(ys, xs) #initialize cost function class with x and y values of the data
        
        # create the initial population: 
        self.pop = population(self.pop_size, self.Nparameters)# creates an empty population
        self.pop.initialize(self.ranges, self.cost)# gives random values to the parameters for each pop member and gets their cost
        
        self.run_optimization() # runs the optimization
        
    
    def get_bests(self): # finds the best cost in the population
        best_index = 0
        #best = self.pop.pop_costs[0]
        #best_set = self.pop.cur_pop[0]
        for i in range(1, self.pop_size):
            if(self.pop.pop_costs[i] < self.pop.pop_costs[best_index]):
                best_index = i
                #best = self.pop.pop_costs[i]
                #best_set = self.pop.cur_pop[i]
        return best_index
    
    def run_optimization(self):
        counter = 0
        cost = self.pop.pop_costs[0]
        while(counter < 20000):
            # note: this updates the population as you go. does not create a new updated population list. 
            for i in range(0, self.pop_size): # will go through each member of the current population to update it
                self.pop.update(i, self.cross_over, self.differential_weight, self.cost) # this will update the member of the population
                counter += 1
            self.best_index = self.get_bests()
            if(counter % 100 and (cost != self.pop.pop_costs[self.best_index]) ):
                self.plot_current_best(counter)
                cost = self.pop.pop_costs[self.best_index]



    def generate_plot_points(self):
        x = -6.0
        dx = (6.0 - -6.0) / 100.0
        xs = []
        fs = []
        for i in range(0, 100):
            f = self.cost.function(self.pop.cur_pop[self.best_index], x)
            x += dx
            fs.append(f)
            xs.append(x)
            
        return xs, fs
            
    def plot_current_best(self, counter):
        xs, fs = self.generate_plot_points()
        print self.pop.cur_pop[self.best_index], self.pop.pop_costs[self.best_index]
        plt.ylim(0, 100)
        plt.xlim(-6, 6)
        plt.plot(xs, fs, linewidth = 2, color = 'r')
        plt.scatter(self.cost.xs, self.cost.ys, s = 8, color = 'b', marker='o')
        plt.savefig('quick_plots/fitting/fit_' + str(counter) + '.png', format='png')
        plt.clf()
        
        
            
        
def main():
    test = test_data()
    #test.plot()
    diff_evo(test.fsn, test.xs)
#main()
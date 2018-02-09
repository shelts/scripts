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
        

class test_data():
    def __init__(self):
        self.N = 30
        self.data_range = [-4.0,4.0]
        self.a = 0.0
        self.b = 25.0
        
        self.A = 50.0
        self.mu = 0
        self.sig = mt.sqrt(0.5)
        
        self.generate_points()
    def func(self, x):
        linear = self.a * x + self.b
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
        
    def initialize(self, ranges):
        for i in range(0, self.size):
            for j in range(0, self.Nparas):
                val = random.uniform(ranges[j].lower, ranges[j].upper)
                self.cur_pop[i].append(val)
            cost = test(self.cur_pop[i])
            self.pop_costs.append(cost)

                 
    def update(self, x, cross_over, differential_weight): 
        a = -1
        b = -1
        c = -1
        while(a == b or a == c or b == c or a == x or b == x or c == x): # pick unique agents
            a = int(random.uniform(0, self.size))
            b = int(random.uniform(0, self.size))
            c = int(random.uniform(0, self.size))
        print a, b, c, x
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
        possible_new_cost = test(possible_new_set)
        if(possible_new_cost < self.pop_costs[x]):# if the new cost is better keep it
            self.cur_pop[x] = possible_new_set
            self.pop_costs[x] = possible_new_cost
        return 0
    
    
class diff_evo:
    class parameter:
        def __init__(self, ranges):
            self.lower = ranges[0]
            self.upper = ranges[1]
                
    def __init__(self):
        self.cross_over = 0.9
        self.differential_weight = 0.8
        self.pop_size = 50
        self.Nparameters = len(search_ranges)
        self.best_index
        self.ranges = []
        
        for i in range(0, self.Nparameters):
            val = self.parameter(search_ranges[i])
            self.ranges.append(val)
        
        # create the initial population: 
        self.pop = population(self.pop_size, self.Nparameters)# creates an empty population
        self.pop.initialize(self.ranges)# gives random values to the parameters for each pop member and gets their cost
        
        self.run_optimization() # runs the optimization
        
    
    def get_bests(self): # finds the best cost in the population
        best_index = 0
        best = self.pop.pop_costs[0]
        best_set = self.pop.cur_pop[0]
        for i in range(1, self.pop_size):
            if(self.pop.pop_costs[i] < best):
                best_index = i
                best = self.pop.pop_costs[i]
                best_set = self.pop.cur_pop[i]
        return best_index
    
    def run_optimization(self):
        counter = 0
        while(counter < 1000):
            # note: this updates the population as you go. does not create a new updated population list. 
            for i in range(0, self.pop_size): # will go through each member of the current population to update it
                self.pop.update(i, self.cross_over, self.differential_weight) # this will update the member of the population
                counter += 1
            self.best_index = self.get_bests()
            self.plot_current_best()
            
    def plot_current_best(self):
        print "NEED TO ADD PLOT CURRENT BEST SECTION"
        
        
        
        
            
        
def main():
    #test = test_data()
    #test.plot()
    diff_evo()
main()
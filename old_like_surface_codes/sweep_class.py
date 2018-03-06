#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */

class sweep_data:
    class sweep_val:
        def __init__(self, parameter_val, likelihood, parameter_val2 = None):
            self.val = parameter_val
            self.lik = likelihood
            if(parameter_val2):
                self.val2 = parameter_val2
            
    def __init__(self, folder, sweep_name, sweep_parameter, dim):
        self.folder = folder
        self.sweep_name = sweep_name
        self.sweep_parameter = sweep_parameter
        self.dim = dim
        self.values = []

        self.parse()
        self.sort()
        
    def parse(self):
        location = self.folder + 'parameter_sweeps' + self.sweep_name + '/' + 'parameter_sweeps' + self.sweep_name
        likelihood_file = open(location + '/' + self.sweep_parameter + '' + '.txt', 'r')
        data_file = open(location + '/' + self.sweep_parameter + '_vals' + '.txt', 'r')
        parameter_vals = []
        if(self.dim == 2):
            parameter_vals2 = []
        likes = []
        counter_l = 0
        counter_g = 0
        
        for line in likelihood_file:
            if (line.startswith("<search_likelihood")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                ss = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                ss = ss[0].split('\n') 
                likes.append(float(ss[0]))
                counter_l += 1
                
        for line in data_file:
            if(self.dim == 1):
                l = float(line)
                parameter_vals.append(l)
            else:
                l = line.split('\t')
                parameter_vals.append(float(l[0]))
                parameter_vals2.append(float(l[1]))
            counter_g +=1
            
        if(counter_l != counter_g):
            print 'WARNING: likelihood_data and parameter_val data length mismatch'
        else:
            self.dataN = counter_l
            
        likelihood_file.close()
        data_file.close()
        
        for i in range(0, len(likes)):
            if(self.dim == 1):
                p = self.sweep_val(parameter_vals[i], likes[i])
            else:
                p = self.sweep_val(parameter_vals[i], likes[i], parameter_vals2[i])
            
            self.values.append(p)
        
        del parameter_vals, likes
        
        if(self.dim > 1):
            del parameter_vals2
    
        return 0
    
    def sort(self): # sorts the data from least to greatest in terms of the first parameter
        val_new = []
        val_tmp = []
        
        unsorted = True
        
        while(unsorted):
            for i in range(0, self.dataN - 1):
                if(self.values[i].val > self.values[i + 1].val):
                    val_tmp  = self.values[i]
                    val_tmp2 = self.values[i + 1]
                    self.values[i] = val_tmp2
                    self.values[i + 1] = val_tmp
                    
            unsorted = False
            for i in range(0, self.dataN - 1):
                diff = self.values[i + 1].val - self.values[i].val
                if(diff >= 0):
                    continue
                else:
                    
                    unsorted = True
        return 0
    
    def plottable_list(self, correct_value):
        self.vals = []
        self.liks = []
        self.corr = []
        self.cor2 = []
        if(self.dim > 1):
            self.vals2 = []
            
        for i in range(0, self.dataN):
            self.vals.append(self.values[i].val)
            self.liks.append(self.values[i].lik)
            self.corr.append(correct_value)
            self.cor2.append(-10.0 * i)
            if(self.dim > 1):
                self.vals2.append(self.values[i].val2)
#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # #
#   Something to run front end to test      #
#    implementation of hessian              #
# # # # # # # # # # # # # # # # # # # # # # #
import matplotlib.pyplot as plt
from test_data import *
from differential_evolution import *
from hessian import *

def plot(test, fit):
    w = 0.25
    plt.figure()
    #plt.xlim(self.lower, self.upper)
    plt.ylim(0, 100)
    plt.ylabel("counts")
    plt.xlabel(r"$\beta_{Orphan}$")
    
    fit_paras = fit.pop.best_paras
    fit_xs, fit_fs = fit.generate_plot_points()
    plt.plot(fit_xs,  fit_fs, color='k',linewidth = 2, alpha = 1., label = 'paras: m=' + str(round(fit_paras[0], 2)) + ' b=' + str(round(fit_paras[1], 2)) + ' A=' + str(round(fit_paras[2], 2)) + r" $x_{0}$=" + str(round(fit_paras[3], 2)) + r' $\sigma$=' + str(round(fit_paras[4], 2)) + ' L=' + str(fit.pop.best_cost) )
    plt.scatter(test.xs, test.fsn, s = 8, color = 'b', marker='o')
    plt.legend()
    plt.savefig('testing_hessian_fit.png', format = 'png')
    plt.close()


def main():
    test = test_data()
    #test.plot()
    fit = diff_evo(test.xs, test.fsn, 20000)
    plot(test, fit)
    parameters = fit.pop.best_paras
    errors = hessian(fit.cost, parameters)


main()
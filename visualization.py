#!/usr/bin/env python

####################################################
# File name: visualization.py                      #
# Author: Parth Mehta, Vidya Venkiteswaran         #
# Email: pm2877@columbia.edu, vv2269@columbia.edu  #
# Date created: 02/26/2017                         #
# Usage: python visualization.py                   #
# Python Version: 3.4, 3.5, 3.6                    #
# Instructor: Prof. Andreas Mueller                #
####################################################

import matplotlib.pyplot as plt

def scatter_plot(X, y):
    """Draw scatter plot

    Draw a scatter plot between different features of housing data
    and target value. Every plot is a matrix 3X3 features

    Parameters
    ----------
    X : pandas
        original data
    y : pandas
        target value

    Returns
    -------
    None
    """

    columns = list(X.columns.values)
    count = 0
    print(X.shape, y.shape)
    while count < len(columns):
        f, ax = plt.subplots(3, 3)
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if count < len(columns):
                    ax[i][j].scatter(X.ix[:, columns[count]], y)
                    ax[i][j].set_xlabel(columns[count])
                    xmin = X.ix[:, columns[count]].min()
                    xmax = X.ix[:, columns[count]].max()
                    # print(columns[count], xmin, xmax)
                    ax[i][j].set_xlim([xmin-1,xmax+1])
                    j += 1
                    count += 1
                else:
                    break
            i += 1
        f.subplots_adjust(hspace=1)
        plt.show()
        
        



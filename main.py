# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:18:34 2016

@author: mmatthew_43
"""
import random
import matplotlib.pyplot as plt
import numpy

def least_squares_method(x, y):
    if(len(x)!=len(y)):
        return "the length of lists does not equal!!"
    left = 0
    for i in range(len(x)):
        left += len(x) * x[i] * y[i]
    
    a_numerator = left - sum(x) * sum(y)
    tmp = 0
    for i in range(len(x)):
        tmp += x[i] * x[i]
    a_denominator = len(x) * tmp - sum(x) * sum(x)
    
    a = a_numerator / a_denominator    
    
    tmp2 = 0
    for i in range(len(x)):
        tmp2 = x[i] * y[i]
    b_numerator = tmp * sum(y) - tmp2 * sum(x)
    b_denominator = len(x) * tmp - sum(x) * sum(x)
    b = b_numerator / b_denominator
    return (a, b)

if __name__ == "__main__":
    print("run")
    a = [random.randrange(1, 100) for x in range(10)]
    print(a)
    b = [random.randrange(1, 100) for x in range(10)]
    print(b)
    coefficients = least_squares_method(a, b)
    print(coefficients)
    
    #y = coefficients[0] * a - coefficients[1]
    
    plt.plot(a, b)
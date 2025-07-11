#!/usr/bin/env python
# coding: utf-8
"""
To check if your solution is correct on a set run the following command(s) in terminal 

    python autograder.py -p even -s small

    python autograder.py -p even -s medium
    
    python autograder.py -p even -s large


run separately for each case
"""

import numpy as np

def even_odd(): # Decide what arguments you want this to take
    """
    even_odd function 
    takes as input one test case 
    returns the solution for the test case (int)
    """
    # Write your Solution Here! 

    raise NotImplementedError 



def run_code(in_name='datasets/small_even_odd_inversion.in'):
    """
    run_code function 
    takes one argument: the sample file to try
    loads the data and writes the solution to the output file (even_sol.out)
    """

    fin = open(in_name, 'r')                  # Do not change
    fout = open('datasets/even_sol.out', 'w')   # Do not change

    fin.close()
    fout.close()

    raise NotImplementedError 



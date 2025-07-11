#!/usr/bin/env python
# coding: utf-8
"""
To check if your solution is correct on a set run the following command(s) in terminal 

    python autograder.py -p course -s small
    
    python autograder.py -p course -s large


run separately for each case

If you get an error: Segmentation Fault, run this command:

    ulimit -s unlimited 


"""

import numpy as np
import sys 
sys.setrecursionlimit(100000000)

def course_selection(): # Decide what arguments this function should take
    """
    course_selection function 
    takes as input one test case loaded from the .in file
    returns the solution for the test case (list, or if there's no possible solution return str(IMPOSSIBLE))
    """
    # Write your Solution Here! 

    raise NotImplementedError 



def run_code(in_name='datasets/course_selection_small.in'):
    """
    run_code function 
    takes one argument: the sample file to try
    loads the data and writes the solution to the output file (course_sol.out)
    """
    fin = open(in_name, 'r')                  # Do not change
    fout = open('datasets/course_sol.out', 'w')   # Do not change

    fin.close()
    fout.close()


    raise NotImplementedError 


#!/usr/bin/env python
# coding: utf-8
"""
To check if your solution is correct on a set run the following command(s) in terminal 

    python autograder.py -p priority -s small
    
    python autograder.py -p priority -s large


run separately for each case
"""

import numpy as np

class PriorityQueue:

    """
    priority class: implement your queue and other helper functions here
    
    """

    def __init__(self):
        
        self.A = []
        

    # Static functions to compute, parent, left and right children.
    # They are implemented as static methods.
    @staticmethod
    def parent(ind):
        return (ind - 1)//2
    
    @staticmethod
    def left(ind):
        return (2*ind)+1
    
    @staticmethod
    def right(ind):
        return (2*ind)+2
    
    def insert(self, x):  
        
        ind = len(self.A)
        self.A.append(x)
        
        if x< -1e6 and x>1e6:
            return
        while self.A[ind] > self.A[self.parent(ind)] and self.parent(ind) >= 0:
            
            self.A[ind], self.A[self.parent(ind)] = self.A[self.parent(ind)], self.A[ind]
            ind = self.parent(ind)
        #return self.A
    
    def fix_heap(self, ind):              # Helper function to fix the heap violated at index ind. See the lecture notes.
        
        n = len(self.A) -1
        L = self.left(ind)
        R = self.right(ind)
        largest = ind
        if L <= n and self.A[L]>self.A[ind]:
            largest = L
        if R<= n and self.A[R] > self.A[largest]:
            largest = R
        if largest != ind:
            b = self.A[ind]
            self.A[ind] = self.A[largest]
            self.A[largest] = b
            #self.A[ind], self.A[largest] = self.A[largest], self.A[ind]
            self.fix_heap(largest)
            
            #print(self.A)
    
     
    # Remove element with max priority
    def extract_maximum(self):
        n = len(self.A)
        if n == 0:
            return
        self.A[0], self.A[n-1] = self.A[n-1], self.A[0]
        self.A.pop(n-1)
        self.fix_heap(0)

    def even_leaves(self):
        n = len(self.A)
        even_leaf = 0
        ind = n-1
        #for ind in range((n//2)+1, n):
        while ind>= 0:
            left_ind = self.left(ind)
            right_ind = self.right(ind)
            if left_ind > (n-1) and right_ind > (n-1):
                if self.A[ind]%2 == 0:
                    even_leaf += 1
            ind -= 1
        return even_leaf
                    
            
        
#Q = PriorityQueue()  
def priority(test_case):
    """
    Priority function
    takes as input one test case
    returns the solution for the test case
    """
    Q = PriorityQueue()
    results = []

    for command in test_case:
        if command[0] == 'I':
            Q.insert(int(command[1]))
        elif command[0] == 'M':
            Q.extract_maximum()
        elif command[0] == 'E':
            results.append(Q.even_leaves())
         

    return results

    
    

    
    


def run_code(in_name='datasets/priority_small.in'):
    """
    run_code function
    takes one argument: the sample file to try
    loads the data and writes the solution to the output file (priority_sol.out)
    """
    fin = open(in_name, 'r')                  # Do not change
    fout = open('datasets/priority_sol.out', 'w')   # Do not change
   
    n_tests = int(fin.readline().strip())  # Read the number of test cases
   
    for _ in range(n_tests):
        k = int(fin.readline().strip())  # Read the number of commands for the current test case
        test_case = []
       
        for _ in range(k):
            command = fin.readline().strip().split()  # Read each command
            test_case.append(command)  # Add the command to the test case list
       
        results = priority(test_case)  # Process the test case using the priority function
       
        for result in results:
            fout.write('%d\n' % result)  # Write each result to the output file
   
    fin.close()  # Close the input file
    fout.close()  # Close the output file


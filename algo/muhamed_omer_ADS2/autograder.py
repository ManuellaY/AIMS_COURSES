import collections
import numpy as np 
import time 
import argparse 



EXTREMELY_SLOW = 5
parser = argparse.ArgumentParser()
parser.add_argument("-s","--size", default="small")
parser.add_argument("-p","--problem", default="even")
args=parser.parse_args()

# The following function takes the input file, the correct output file, and the student's solution file,
# And returns True or False
def check_file(inp, out, std):

  ## Check if student's file is in the right format
  # each line contains a list of int sep by space, or Impossible
  student = open(std, 'r')
  nl = 0
  for line in student.readlines():
    nl += 1
    line = line.split()
    if len(line) == 0:
      raise Exception("Student's file in wrong format")
    if line[0].lower() == "impossible":
      continue
    line = map(int, line)  # handle
  student.close()

  inp = open(inp, 'r')
  out = open(out, 'r')
  std = open(std, 'r')
  # Check solution
  result = []
  n_tests = int(inp.readline())
  for i in range(n_tests):
    n, m = map(int, inp.readline().split())
    Cons = []
    for j in range(m):
      temp = inp.readline().split()
      temp = tuple(map(int, temp))
      Cons.append(temp)

    correct = out.readline().split()
    student = std.readline().split() # empty if EOF
    if correct[0] == "Impossible":
      if len(student) == 0 or student[0].lower() != "impossible":
        result.append(False)
      else:
        result.append(True)
    else:
      if len(student) == 0 or student[0].lower() == "impossible":
        result.append(False)
      else:
        student = list(map(int, student))
        result.append(check_solution(n, Cons, student))
  inp.close()
  out.close()
  std.close()


  c = 0
  for test in range(1, n_tests+1):
    if result[test-1]:
        c += 1
    #print("Test {:d} : {:s}".format(test, str(result[test-1])))
  p = c/len(result)*100
  return all(result), p


# Several solutions may exists for some input.
# The following function checks a solution against some input.
# Assumes that Solution != "Impossible"
def check_solution(n, Cons, Solution):
	if type(Solution) != list:
		# raise Exception("Unexpected Solution {}".format(Solution))
		return False

	# The solution is correct if for every constraint (i, j),
	# the task i appears before the task j in Solution.
	# Also, we should make sure that every task in Solution is valid and appears exactly once.

	# Checking that every task in Solution is valid and executed exactly once
	executed = [False] * n
	for task in Solution:
		if not (1 <= task <= n): # task is invalid
			# raise Exception("Unknown Task {:d} . Expecting 1 <= task <= {:d}".format(task, n))
			return False
		if executed[task-1]: # task appears twice
			# raise Exception("Task {:d} is executed more than once".format(task))
			return False
		executed[task-1] = True

	for index, is_executed in enumerate(executed):
		if not is_executed:
			# raise Exception("Task {:d} is not executed".format(index+1))
			return False

	# Checking that the order of execution is valid
	rank = [0] * n
	for index, task in enumerate(Solution):
		rank[task-1] = index
	for (i, j) in Cons:
		if rank[i-1] > rank[j-1]: # i should not be executed before j !
			# raise Exception("Solution does not satisfy constraint ({:d},{:d})".format(i, j))
			return False
	return True



if args.problem == "even":
    from even import run_code as even 
    if args.size == "small":
        in_name = 'datasets/small_even_odd_inversion.in'
        out_name = "datasets/small_even_odd_inversion.out"

    elif args.size == "medium":
        in_name = 'datasets/medium_even_odd_inversion.in'
        out_name = "datasets/medium_even_odd_inversion.out"


    elif args.size == "large":
        in_name = 'datasets/large_even_odd_inversion.in'
        out_name = "datasets/large_even_odd_inversion.out"

    else:
        print("Invalid Option: You can only run small, medium, or large tests for this problem!")

    start_time = time.time()
    even(in_name)
    end_time = time.time()

    time_taken = end_time - start_time

    print("Time taken to execute this script was: ", time_taken, "Seconds!" )

    if time_taken > EXTREMELY_SLOW:
        print("Your code is very very slow!")


    s_list = []

    with open('datasets/even_sol.out','r') as sol:
        for s in sol:
            l = s.split(' ')
            s_list.append(l)

    o_list = []    

    with open(out_name,'r') as out:
        for o in out:
            l = o.split(' ')
            o_list.append(l)


    assert len(o_list) == len(s_list), "The length of your output file is incorrect!"

    correct = 0
    
    for i,j in zip(o_list, s_list):

        if collections.Counter(i) == collections.Counter(j):
            correct += 1
    if correct/len(o_list) == 1.0:
        print("Your Solution is Correct on the",  args.size ,"Dataset for the Even-Odd Inversion Problem!")
    
    else:
        print("Your Solution Passed Only ", correct/len(o_list)*100, "Percent of the Given Test Cases!" )

if args.problem == "connections":
    from close_connections import run_code as connections 
    if args.size == "small":
        in_name = 'datasets/connections_small.in'
        out_name = "datasets/connections_small.out"

    elif args.size == "large":
        in_name = 'datasets/connections_large.in'
        out_name = "datasets/connections_large.out"


    else:
        print("Invalid Option: You can only run small or large tests for this problem!")

    start_time = time.time()
    connections(in_name)
    end_time = time.time()

    time_taken = end_time - start_time

    print("Time taken to execute this script was: ", time_taken, "Seconds!" )
    if time_taken > EXTREMELY_SLOW:
        print("Your code is very very slow!")
    
    s_list = []

    with open('datasets/connections_sol.out','r') as sol:
        for s in sol:
            l = s.split(' ')
            s_list.append(l)

    o_list = []    

    with open(out_name,'r') as out:
        for o in out:
            l = o.split(' ')
            o_list.append(l)


    assert len(o_list) == len(s_list), "The length of your output file is incorrect!"

    correct = 0
    
    for i,j in zip(o_list, s_list):

        if collections.Counter(i) == collections.Counter(j):
            correct += 1
    if correct/len(o_list) == 1.0:
        print("Your Solution is Correct on the",  args.size ,"Dataset for the Close Connections Problem!")
    
    else:
        print("Your Solution Passed Only ", correct/len(o_list)*100, "Percent of the Given Test Cases!" )


if args.problem == "course":
    from course_selection import run_code as course 
    if args.size == "small":
        in_name = 'datasets/course_selection_small.in'
        out_name = "datasets/course_selection_small_sol.out"


    elif args.size == "large":
        in_name = 'datasets/course_selection_large.in'
        out_name = "datasets/course_selection_large_sol.out"

    else:
        print("Invalid Option: You can only run small or large tests for this problem!")

    start_time = time.time()
    course(in_name)
    end_time = time.time()

    time_taken = end_time - start_time

    print("Time taken to execute this script was: ", time_taken, "Seconds!" )
    if time_taken > EXTREMELY_SLOW:
        print("Your code is very very slow!")
    checker, p = check_file(in_name, out_name, 'datasets/course_sol.out')

    if checker: 
        print("Your Solution is Correct on the",  args.size ,"Dataset for the Course Selection Problem!")
        
    else:
        print("Your Solution is Only Correct for ", p, "Percent of the Test Cases!")


if args.problem == "priority":
    from priority import run_code as connections 
    if args.size == "small":
        in_name = 'datasets/priority_small.in'
        out_name = "datasets/priority_small.out"

    elif args.size == "large":
        in_name = 'datasets/priority_large.in'
        out_name = "datasets/priority_large.out"


    else:
        print("Invalid Option: You can only run small or large tests for this problem!")

    start_time = time.time()
    connections(in_name)
    end_time = time.time()

    time_taken = end_time - start_time

    print("Time taken to execute this script was: ", time_taken, "Seconds!" )
    if time_taken > 60:
        print("Your code is very very slow!")
    
    s_list = []

    with open('datasets/priority_sol.out','r') as sol:
        for s in sol:
            l = s.split(' ')
            s_list.append(l)

    o_list = []    

    with open(out_name,'r') as out:
        for o in out:
            l = o.split(' ')
            o_list.append(l)


    assert len(o_list) == len(s_list), "The length of your output file is incorrect!"

    correct = 0
    
    for i,j in zip(o_list, s_list):

        if collections.Counter(i) == collections.Counter(j):
            correct += 1
    if correct/len(o_list) == 1.0:
        print("Your Solution is Correct on the",  args.size ,"Dataset for the Priority Problem!")
    
    else:
        print("Your Solution Passed Only ", correct/len(o_list)*100, "Percent of the Given Test Cases!" )

# CS473 Adv. Algorithms Final Project Group Eagles
# Aaron Borjas, Connor Weldy, Jorjei Ngoche
# In this project, we are aiming to complete a scheduling problem using graph coloring. In our situation, we are aiming to schedule classes for
# a single department of a university. We consider professors, classes, classrooms, and timeslots to complete this problem. 
# We have two methods that we are aiming to accomplish: prioritizing student constraints (e.g. classes earlier in the day, no conflicting classes) 
# and prioritizing professors' constraints (e.g. preferred classes to teach).

'''
0. prof constraints {'p1': ['c7', 'c1', 'c4'], 'p2': {'c5', 'c2'}, 'p3': {'c3', 'c6'}}
1. class constraints: {c7: {c1, c5}, c5: {c7,c1}, c1: {c7,c5}}
2. class const: [('c1', 'c3'), ('c2','c3')]

3. combine structre {c7: {c1, c5}, c5: {c7,c1}, c1: {c7,c5, c3}}

4. copy the value sets to a list
'''

import math
import random
from graph_color import *
from course import *
from course_constrainer import *

#TODO intialize elsewhere (not in main.py)
### Driver code
course_constr = Course_Constrainer()
course_constr.add_courses(['C1','C4','C7','C2','C5','C8','C3','C6'])
profs = ['P1', 'P2', 'P3']
class_constraints = [('C1', 'C4'), ('C2', 'C7'), ('C6', 'C8'), ('C1', 'C8')]
course_constr.add_profs(profs)
course_constr.add_course_constraints(class_constraints)


x = course_constr.gen_graph()
print(x)
#create_graph_coloring_greedy(x)

# # Assign classes to profs randomly
# prof_to_class_dict = random_assign_class_to_profs(classes, profs)
# print(prof_to_class_dict)

# # generate graph adjacency list with both implicit and explicit
# graph_adj_list = gen_graph(prof_to_class_dict, class_constraints)
# print(graph_adj_list)


# class2 = Course()
# class1 = Course('p1', 'blue')
# print(helloworld()) #LIAR
# print(class1, class2)
#print(class2.color)

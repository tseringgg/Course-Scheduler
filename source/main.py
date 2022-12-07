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
#using sample data from Nate Moyer for CS 2023-2024 school year...
'''
Profs: Kent Jones, Qian Mao, Scott Griffith, Matt Bell, Pete Tucker (5 total)

Classes (fall): 
    CS125 x2, CS171 x4, CS172 x1, CS200 x1, CS273 x2, CS274 x1, CS278 x1, CS313 x1, 
    CS333 x1, CS344 x1, CS359 x1, CS370 x1, CS373 x1, CS374 x1, CS471 x1, CS473 x1
    21 total classes in the fall


Classes (spring): 
    CS125 x2, CS171 x2, CS172 x2, CS251 x1, CS273 x1, CS274 x1, CS278 x1, CS314 x1,
    CS374 x1, CS375 x1, CS378 x1, CS401 x1, CS457 x1, CS472 x1, CS475 x1
    18 total classes offered in the spring


Time slots (fall): 
    MWF - 8-8:55am, 9:05-10am, 10:25-11:20am, 11:45am-12:40pm, 12:50-1:45pm (5 timeslots)
    TTh - 8-9:20am, 9:30-10:50am, 12:50-2:50pm, 4-6pm, 6-6:55pm (5 timeslots)
Time slots (spring):
    MWF - 8-8:55am, 9:05-10am, 10:25am-11:20am, 11:45am-12:40pm, 12:50-1:45pm, 1:55-2:10pm, 6:30-9pm (7 timeslots)
    TTH - 8-9:20am, 9:30-10:50am, 12:50-2:10pm, 2:20-3:40pm (4 timeslots)
'''
'''
Profs: Kelsey Marcinko, Lindy Moyer, Martha Gady, Diana Schepens, Jordan Broussard, Nate Moyer, Immanual Manohar,
       Molly Lamb, Steve Gady, Lyle Cochran (10 total)

Classes (fall): 
    MA/CS294, MA/CS499, MA107 x2, MA108 x2, MA130, MA150 x2, MA171 x4, MA172 x2, MA221, MA222, MA256 x2,
    MA273 x2, MA278, MA281, MA306, MA330, MA357, MA410
Classes (spring): 
    MA107, MA108, MA130, MA150, MA158, MA171 x2, MA172 x3, MA221, MA222, MA256 x3, MA273, MA278, MA281, 
    MA330, MA350, MA358, MA365, MA411, MA430

Time slots (fall):
    MWF - 8-8:55am, 9:05-10am, 10:25-11:20am, 11:45am-12:40pm, 12:50-1:45pm, 1:55-2:50pm (6 timeslots)
    TTH - 8-9:20am, 9:30-10:50am (2 timeslots)
Time slots (spring):
    MWF - 8-8:55am, 9:05-10am, 10:25-11:20am, 11:45am-12:40pm, 12:50-1:45pm, 1:55-2:50pm (6 timeslots)
    TTH - 8-9:20am, 9:30-10:50am (2 timeslots)
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

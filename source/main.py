#CS473 Adv. Algorithms Final Project Group Eagles
#Aaron Borjas, Connor Weldy, Jorjei Ngoche
#In this project, we are aiming to complete a scheduling problem using graph coloring. In our situation, we are aiming to schedule classes for
#a single department of a university. We consider professors, classes, classrooms, and timeslots to complete this problem. 
#We have two methods that we are aiming to accomplish: prioritizing student constraints (e.g. classes earlier in the day, no conflicting classes) and prioritizing professor '
#   constraints (e.g. preferred classes to teach).

import math
import random

# create_graph_coloring_greedy function - colors a graph using a greedy algorithm. uses https://iq.opengenus.org/graph-colouring-greedy-algorithm/ as a reference
# input: an dictionary adjacency list representation of a graph, where the vertices are classes and edges are incompatibilities. 
#        e.g. c1---c2 means c1 and c2 can't be at the same time
#        the input graph may look like: {1: [2, 4], 2: [3], 3: [1], 4: [1]}
# output: returns a dictionary where keys are vertices and values are letters (colors)
#         output may look like {1: a, 2: b, 3: c, 4: b} for the above sample graph
def create_graph_coloring_greedy(adj_list):
    print("hello world")

# random_assign_class_to_profs function
# Purpose: assign classes to profs in a random fashion, equally distributing classes to profs
# input: list of classes
#        list of profs
# output: dictionary containing profs as keys and values as list of classes
def random_assign_class_to_profs(class_list, prof_list):
    prof_to_class_dict = {}
    random.shuffle(class_list) # shuffle the classes in class_list for randomization :)
    print(classes)
    #https://stackoverflow.com/questions/53144723/python-evenly-distribute-value-to-a-list-in-a-dictionary  
    #Lst[ Initial : End : IndexJump ]
    # for (index of prof) and (prof) in prof_list => (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    for idx, prof in enumerate(prof_list):
        # gets every (number of profs)th class in class list and adds to list stored in value of dictionary
        prof_to_class_dict[prof] = class_list[idx::len(prof_list)]
    return prof_to_class_dict

classes = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']
profs = ['p1', 'p2', 'p3']

print(random_assign_class_to_profs(classes, profs))

# pref_assign_class_to_profs function
# Purpose: assign classes to profs using professor preferences, attempting to equally distribute classes to profs
# input: list of classes
#        list of profs
#        professor preferences
# output: dictionary containing profs as keys and values as list of classes
def pref_assign_class_to_profs(class_list, prof_list, prof_preferences):
    prof_to_class_dict = {}
    return prof_to_class_dict


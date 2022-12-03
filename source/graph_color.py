# CS473 Group Eagles final project - Aaron Borjas, Connor Weldy, Jorjei Ngoche
# 12/2/2022
# This file does the graph coloring stuff for our project
# create_graph_coloring_greedy function - colors a graph using a greedy algorithm. uses https://iq.opengenus.org/graph-colouring-greedy-algorithm/ as a reference
# input: an dictionary adjacency list representation of a graph, where the vertices are classes and edges are incompatibilities. 
#        e.g. c1---c2 means c1 and c2 can't be at the same time
#        the input graph may look like: {1: [2, 4], 2: [3], 3: [1], 4: [1]}
#        later we can implement stuff like time slots available and rooms available
# output: returns a set of Courses, with all items having the color assigned using graph
#           coloring methods.
def create_graph_coloring_greedy(adj_list, start_course):
    # Color first vertex with first color
    # Repeat following for V-1 times:
    # - consider the currently picked vertex
    # - color it with lowest numbered color not used by previously colored vertices adjacent to it
    # - if all previously used colors appear on vertices adjacent to v, assign a new color it
    course_colors = {c:-1 for c in adj_list.keys()}


    print("hello world")
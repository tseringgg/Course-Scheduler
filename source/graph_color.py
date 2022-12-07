# CS473 Group Eagles final project - Aaron Borjas, Connor Weldy, Jorjei Ngoche
# 12/2/2022
# This file does the graph coloring stuff for our project
from course import *

#assigns the course to a room based on the room assignments of other classes (basically greedy coloring)
#inputs - current course class that doesn't have a room assigned, number of rooms available, 
#         number of rooms available in total as an integer, and a list of neighbors to the course
#outputs - no return values but sets the room value of the current course (colors it)
def set_timeslot(current_course, num_avail_timeslots, neighbor_timeslot):
    max_room = 0
    #courses_per_timeslot
    #while current_course.get_room() == -1: #while the course's room not set
    for timeslot in range(1,num_avail_timeslots+1):

        # check how many times r has been used
        
        if timeslot not in neighbor_timeslot:
            current_course.set_timeslot(timeslot)
            max_room = timeslot
            break
    return max_room
    

# create_graph_coloring_greedy function - colors a graph using a greedy algorithm. uses https://iq.opengenus.org/graph-colouring-greedy-algorithm/ as a reference
# input: an dictionary adjacency list representation of a graph, where the vertices are classes and edges are incompatibilities. 
#        e.g. c1---c2 means c1 and c2 can't be at the same time
#        input graph will just be a list of course objects, which have a member variable
#           that contains all neighbors
#        later we can implement stuff like time slots available and rooms available
# output: returns a set of Courses, with all items having the color assigned using graph
#           coloring methods.
def create_graph_coloring_greedy(adj_list, num_avail_rooms):
    # Color first vertex with first color
    # Repeat following for V-1 times:
    # - consider the currently picked vertex
    # - color it with lowest numbered color not used by previously colored vertices adjacent to it
    # - if all previously used colors appear on vertices adjacent to v, assign a new color it
    
    '''
    PSEUDO CODE
    bfs approach - bfs to find nodes to color then separate color checker for adj to node n

    add first node to queue
    for course in list:
        check if course is colored, if not then add to queue
        while queue
            course = pop(0)
            if course no room
                # get neighbor rooms
                # choose lowest numbered room available
                # adding neigbors to queue that arent colored and not already in queue
    
    '''
    #graph coloring with BFS
    #adj_list[0].set_room(1)
    bfs_queue = []
    for course in adj_list: #make sure we cover all the courses
        if course.get_room() == -1: # if course does not have a room yet
            bfs_queue.append(course) # add to end of queue
        while bfs_queue: #while the queue isnt empty
            current_course = bfs_queue.pop(0) # get first course from queue
            if current_course.get_room() == -1: # if course does not have a room yet
                # Get rooms of neighbors:
                neighbor_timeslot = current_course.get_neighbor_timeslots()
                print(current_course.course_id)
                print(neighbor_timeslot)
                print(current_course.get_neighbors())
                # Set the room to the course
                set_timeslot(current_course, num_avail_rooms, neighbor_timeslot)
                # Add neighbor nodes that don't have a room
                for neighbor_course in current_course.get_neighbors():
                    #add the neighbor_course to the queue if the course isn't in the queue
                    #and if the course has not been assigned a room yet.
                    if neighbor_course not in bfs_queue and neighbor_course.get_timeslot() == -1:
                        bfs_queue.append(neighbor_course)

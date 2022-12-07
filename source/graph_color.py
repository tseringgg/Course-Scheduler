# CS473 Group Eagles final project - Aaron Borjas, Connor Weldy, Jorjei Ngoche
# 12/2/2022
# This file does the graph coloring stuff for our project
from course import *

def get_neighbor_rooms(course):
    available_rooms = []
    for neighbor in course.get_neighbors():
        if neighbor.get_room() != -1: #if the course was assigned to a room
            available_rooms.append(neighbor.get_room())


# create_graph_coloring_greedy function - colors a graph using a greedy algorithm. uses https://iq.opengenus.org/graph-colouring-greedy-algorithm/ as a reference
# input: an dictionary adjacency list representation of a graph, where the vertices are classes and edges are incompatibilities. 
#        e.g. c1---c2 means c1 and c2 can't be at the same time
#        input graph will just be a list of course objects, which have a member variable
#           that contains all neighbors
#        later we can implement stuff like time slots available and rooms available
# output: returns a set of Courses, with all items having the color assigned using graph
#           coloring methods.
def create_graph_coloring_greedy(adj_list):
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
    
    #we got confused by this code so commenting to restart
    # rooms = [-1 for i in range(0,100)] # colors
    
    # bfs_queue = []
    
    # adj_list[0].set_room(rooms[0])
    
    # for course in adj_list: #make sure all courses are evaluated (disconnected courses)
    #     bfs_queue.append(course)
    #     while bfs_queue: #while the queue isn't empty (doing BFS)
            
    #         current_course = bfs_queue.pop(0)
    #         if current_course.get_room() == -1: # not colored
    #             print("hi") 
    #             #color room appropriately
    #             # get smallest room value not used
    #             # check neighbor nodes 
    #             # 
    #         # coloring
            
    #         for neighbor in course.get_neighbors(): #find available colors
    #             bfs_queue.append(neighbor)
                
        

    '''
    brute force approach

    for course in adj_list:
        # if no room
            # get neighbor rooms
            # choose lowest numbered room available
        # otherwise skip

    -----------------------------------------

        

    
    '''




    print("hello world")

#BFS reference from Aaron's Rosalind 10
#start node is always vertex 1
#this function references Kent Jones' slide 1-32 from Chapter 3: brute force to solve the BFS problem
def BFS():
    verts = parseVertices() #keys = vertices value = list of vertices key points to
    print(verts)

    #setting up the problem
    countVert = dict.fromkeys(range(1, len(verts)+1), False) #{k: False for k in len(verts)} #list of all vertices w/ 0 count attached
    solution = dict.fromkeys(range(1, len(verts)+1), -1) #{k: -1 for k in len(verts)}#list of all verts and distance from node 1
    solution[1] = 0 #distance from 1 to itself is 0
    bfsQueue = []
    #bfsQueue.append(1)

    for v in range(1, len(verts)+1):
        bfsQueue.append(v)
        while(len(bfsQueue) > 0): #goes until the queue is empty (no more verts to find)

            #print(solution)
            currNode = bfsQueue.pop() #the current node of which to evaluate neighbors of

            if(countVert[currNode] == False): #if the current vertex has not been evaluated

                countVert[currNode] = True #set the vertex as evaluates

                for m in verts.get(currNode): #for every neighbor of the current vertex

                    if countVert[m] == False: #if the neighbor is not visted
                        #if hasRoot(m, 1, verts):
                        #countVert[m] = True
                        if solution[currNode] != -1:
                            solution[m] = solution[currNode]+1
                        bfsQueue.append(m) #add the neighbor to the queue

    return solution
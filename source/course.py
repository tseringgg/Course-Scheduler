#12/10/2022 by Aaron Borjas, Connor Weldy, Jorjei Ngoche for CS473 adv. algorithms taught by Dr. Kent Jones
#helper class to organize our data in the scheduling/graph coloring final project.
class Course:
    def __init__(self, course_id='default course', c_name='default name'):
        self.course_id = course_id
        self.course_name = c_name
        self.professor = 'no professor'
        self.timeslot = -1 # color in graph
        self.room = -1
        self.neighbors = [] #list of classes that cannot be at the same time as the current instance
    
    #https://stackoverflow.com/questions/12933964/printing-a-list-of-objects-of-user-defined-class
    #useful for simplying printing lists of Courses. Stackoverflow explained this.
    def __repr__(self):
        return self.course_id
    
    #function for displaying information of a course
    def __str__(self):
        #return self.course_id
        return f"ID: {self.course_id}, Course: {self.course_name}, Prof: {self.professor}, Timeslot: {self.timeslot}, Room: {self.room}"
    
    #=========== various getters and setters ==============

    def add_neighbor(self, course):
        self.neighbors.append(course)
    
    def remove_neighbor(self,course):
        self.neighbors.remove(course)
    
    def clear_neighbors(self):
        self.neighbors.clear()
    
    def set_professor(self, professor):
        self.professor = professor
    
    def get_professor(self):
        return self.professor
    
    def set_timeslot(self, time):
        self.timeslot = time

    def set_room(self, room):
        self.room = room

    def get_room(self):
        return self.room
    
    def get_course_id(self):
        return self.course_id

    def get_neighbors(self):
        return self.neighbors

    def get_timeslot(self):
        return self.timeslot
    
    def get_name(self):
        return self.course_name

    #another getter but gets the specific timeslots (colors) of the neighbors
    def get_neighbor_timeslots(self):
        neighbor_timeslots = set()
        for n in self.neighbors:
            neighbor_timeslots.add(n.timeslot)
        return neighbor_timeslots
        
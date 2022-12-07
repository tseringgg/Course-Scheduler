
#helper class to organize our data in the scheduling/graph coloring final project.
class Course:
    def __init__(self, course_id='default course'):
        self.course_id = course_id
        self.professor = 'no professor'
        self.timeslot = 'none' # color in graph
        self.room = -1
        self.neighbors = [] #list of classes that cannot be at the same time as the current instance
    
    #https://stackoverflow.com/questions/12933964/printing-a-list-of-objects-of-user-defined-class
    #useful for simplying printing lists of Courses. Stackoverflow explained this.
    def __repr__(self):
        return self.course_id
    
    def __str__(self):
        #return self.course_id
        return f"Prof: {self.professor}, Timeslot: {self.timeslot}, Room: {self.room}"
    
    def add_neighbor(self, course):
        self.neighbors.append(course)
    
    def set_professor(self, professor):
        self.professor = professor
    
    def set_timeslot(self, time):
        self.timeslot = time
    
    def set_room(self, room):
        self.room = room

    def get_room(self):
        return self.room
    
    def get_neighbors(self):
        return self.neighbors
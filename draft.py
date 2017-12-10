from pyswip import Prolog
p = Prolog()

class Lecturer:
    def __init__(self, code, name, time, course, sched = None):
        self.lectCode = code #string
        self.lectName = name #string
        self.lectTime = time #list of time objects
        self.lectCourse = crse #list of course objects

class Time:
    def __init__(self, times):
        self.times = times #for example, (0, [9,10,11,12,13,14]) 0=Sunday,
        
class Course:
    def __init__(self, code, name, time, lect, facilities, sched = None):
        self.crsCode = code #string
        self.crsName = name #string
        self.crsTime = time #list of time objects
        self.facilities = []
        self.crsCourse = lect #lecturer

class Schedule:
    
class Room:

class StudentGroup:


def buildProlog(lecturers, room, studentGroup, course):
    

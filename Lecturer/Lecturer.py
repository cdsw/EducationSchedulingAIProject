class Lecturer:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
        self.Courses = []

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getName(self):
        return self.Name

    def setName(self, Name):
        self.Name = Name

    def getCourses(self):
        return self.Courses

    def addCourse(self, course):
        self.Courses.append(course)

    def delCourse(self, course):
        self.Courses.remove(course)
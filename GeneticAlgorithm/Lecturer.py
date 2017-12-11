class Lecturer:
    def __init__(self, lecturer_name, preference_timeslot):
        self.lecturer_name = lecturer_name
        self.preference_timeslot = preference_timeslot
        self.course_timeslot = [[],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[]]

    def place_course(self, position, course):
            self.course_timeslot[position].append(course)

    def print_timeslot(self):
        count = 0
        print('[', end=' ')
        for i in self.course_timeslot:
            print(i , end = ', ')
            count += 1
            if(count % 3 == 0):
                print()
        print(']')
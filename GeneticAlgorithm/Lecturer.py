class Lecturer:
    def __init__(self, lecturer_name, preference_timeslot):
        self.lecturer_name = lecturer_name
        self.preference_timeslot = preference_timeslot
        self.course_timeslot = [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0]

    def place_course(self, position, course):
        if (self.course_timeslot[position] == 0):
            self.course_timeslot[position] = [course]

        else:
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
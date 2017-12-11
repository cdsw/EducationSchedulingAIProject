class StudentGroup:

    def __init__(self, student_group):
        self.student_group = student_group
        self.student_group_timeslot = [[],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[]]

    def place_course(self, position, course):
        self.student_group_timeslot[position].append(course)

    def print_timeslot(self):
        count = 0
        print('[', end=' ')
        for i in self.student_group_timeslot:
             print(i , end = ', ')
             count += 1
             if (count % 3 == 0):
                 print()

        print(']')
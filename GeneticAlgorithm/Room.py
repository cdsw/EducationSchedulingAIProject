class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.room_timeslot = [[],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[]]

    def place_course(self, position, course):
        self.room_timeslot[position].append(course)

    def print_timeslot(self):
        count = 0
        print('[', end=' ')
        for i in self.room_timeslot:
            print(i , end = ', ')
            count += 1
            if (count % 3 == 0):
                print()
        print(']')
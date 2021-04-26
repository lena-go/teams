import csv
import datetime
import itertools
from math import ceil

# import datetime as dt
# start="09:35:23"
# end="10:23:00"
# start_dt = dt.datetime.strptime(start, '%H:%M:%S')
# end_dt = dt.datetime.strptime(end, '%H:%M:%S')
# diff = (end_dt - start_dt)
# diff.seconds/60

# def get_minutes_in_period(period: ('datetime', 'datetime')) -> int:
#     pass


class Participant:
    def __init__(self, name: str):
        self.name = name
        self.periods: [('datetime', 'datetime')] = []
        self.duration: int


class Meeting:
    def __init__(self, incorrect_period: ('datetime', 'datetime'), total_participants):
        self.total_participants = total_participants
        self.incorrect_period = incorrect_period
        self.correct_period: ('datetime', 'datetime')
        self.timeline: [int]
        self.participants: ['Participant'] = []

    def add_participant(self, person: 'Participant'):
        self.participants.append(person)

    def get_correct_period(self, percentage):
        self.set_timeline()
        for person_ in self.participants:
            for time in person_.periods:
                self.mark_timeline(time)  #does smth. with self.timeline
        correct_period = self.compute_correct_period(percentage)
        #return correct_period

    def set_timeline(self):
        minutes = (self.incorrect_period[1] - self.incorrect_period[0]).seconds // 60 + 1
        self.timeline = [0 for i in range(minutes)]

    def mark_timeline(self, time):
        timepoint_0 = (time[0] - self.incorrect_period[0]).seconds // 60
        timepoint_1 = (time[1] - self.incorrect_period[0]).seconds // 60
        for minute in range(timepoint_0, timepoint_1 + 1):
            self.timeline[minute] += 1

    def compute_correct_period(self, percentage):
        for minute in range(len(self.timeline)):
            # округляем до 2 знаков после запятой:
            self.timeline[minute] = round(self.timeline[minute] / self.total_participants * 100, 2)
            print(self.timeline)


if __name__ == '__main__':
    way = 'meetingAttendanceReport(General) (3).csv'
    with open(way, 'r', encoding='utf16') as f_obj:  # открытие файла
        reader = csv.reader(f_obj, delimiter='\t')
        file = []  # это сам файл в виде массива

        strings = 0
        for row in reader:  # здесь считается количество непустых строк в файле
            file.append(row)
            strings += 1

        number_of_users = file[1][1]  # это количество участников

        users = []
        for i in range(7, strings):  # это массив со списком участников (без повторений)
            users.append(file[i][0])
        users = list(set(users))

    meeting = Meeting((datetime.datetime.strptime(file[3][1], "%d.%m.%Y, %H:%M:%S"),
                       datetime.datetime.strptime(file[4][1], "%d.%m.%Y, %H:%M:%S")),
                      int(file[1][1]))

    name_is_unique = True
    for row in range(7, strings):
        name_ = file[row][0]

        person = None
        for participant in meeting.participants:
            if participant.name == name_:
                name_is_unique = False
                person = participant
                break

        if name_is_unique:
            person = Participant(file[row][0])
            meeting.add_participant(person)

        time0 = datetime.datetime.strptime(file[row][1], "%d.%m.%Y, %H:%M:%S")
        time1 = datetime.datetime.strptime(file[row][2], "%d.%m.%Y, %H:%M:%S")
        person.periods.append((time0, time1))

        name_is_unique = True

    meeting.get_correct_period(20)

import csv
import datetime

# import datetime as dt
# start="09:35:23"
# end="10:23:00"
# start_dt = dt.datetime.strptime(start, '%H:%M:%S')
# end_dt = dt.datetime.strptime(end, '%H:%M:%S')
# diff = (end_dt - start_dt)
# diff.seconds/60

def get_minutes_in_period(period: ('datetime', 'datetime')) -> int:
    pass


class Participate:
    def __init__(self, name: str, period: [('datetime', 'datetime')]):
        self.name = name
        self.period = period
        self.duration: int


class Meeting:
    def __init__(self, incorrect_period: ('datetime', 'datetime')):
        self.incorrect_period = incorrect_period
        self.correct_period: ('datetime', 'datetime')
        self.timeline: [int]
        self.participates: ['Participate'] = []

    def add_participate(self, person: 'Participate'):
        self.participates.append(person)

    def get_correct_period(self):
        self.timeline = self.set_timeline()
        for person in self.participates:
            for time in person.period:
                self.mark_timeline(time)  #does smth. with self.timeline
        correct_period = self.compute_correct_period()
        return correct_period

    def set_timeline(self):
        minutes = get_minutes_in_period()
        self.timeline = [0 for i in range(minutes)]

    def mark_timeline(self, time):
        pass

    def compute_correct_period(self):
        pass


minutes_of_meeting = 90  # function
timeline = [0 for i in range(minutes_of_meeting)]

# def mark_timeline(meeting_time, member, timeline):
#     pass

def compute_meeting_period(meeting_time: 'datetime', timeline: [int], members_time: ['datetime']):
    for member in members_time:
        mark_timeline(meeting_time, member, timeline)


if __name__ == '__main__':
    file_name = 'meetingAttendanceReport(General) (3).csv'
    with open(file_name, newline='', encoding='utf-16') as csvfile:
        teamsreader = csv.reader(csvfile, delimiter='\t')
        for row in teamsreader:
            print(', '.join(row))

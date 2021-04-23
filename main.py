import csv
import datetime


class Participate:
    def __init__(self):
        self.period : 'datetime'


class Meeting:
    def __init__(self):
        self.timeline = [0 for i in range(minutes_of_meeting)]
        self.participates = []

    def add_participate(self, person: 'Participate'):
        self.participates.append(person)


minutes_of_meeting = 90  # function
timeline = [0 for i in range(minutes_of_meeting)]

def mark_timeline(meeting_time, member, timeline):
    pass

def compute_meeting_period(meeting_time: 'datetime', timeline: [int], members_time: ['datetime']):
    for member in members_time:
        mark_timeline(meeting_time, member, timeline)


if __name__ == '__main__':
    file_name = 'meetingAttendanceReport(General) (3).csv'
    with open(file_name, newline='', encoding='utf-16') as csvfile:
        teamsreader = csv.reader(csvfile, delimiter='\t')
        for row in teamsreader:
            print(', '.join(row))

from goal import Goal
from datetime import date

class TimeGoal(Goal):
    def __init__(self, title: str, startdate:date, deadline:date):
        super().__init__(title)
        self._startdate = startdate
        self._deadline = deadline

    def get_startdate(self):
        return self._startdate

    def get_deadline(self):
        return self._deadline

    def calculate_remaining_time(self):
        remaining_time = self._startdate - self._deadline
        return remaining_time

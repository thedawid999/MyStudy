from goal import Goal
from datetime import date

class TimeGoal(Goal):
    def __init__(self, title: str, startdate:str, deadline:str):
        super().__init__(title)
        self._startdate = date.fromisoformat(startdate)
        self._deadline = date.fromisoformat(deadline)

    def get_startdate(self):
        return self._startdate

    def get_deadline(self):
        return self._deadline

    def calculate_duration(self):
        duration = (self._deadline - self._startdate).days
        return duration

    def calculate_remaining_time_percentage(self):
        if date.today() < self._startdate:
            return 0
        else:
            duration = self.calculate_duration()
            percentage = ((date.today() - self._startdate).days / duration)*100
            return percentage

    def calculate_days_left(self):
        return (self._deadline - date.today()).days

    @staticmethod
    def to_timegoal(data):
        return TimeGoal(data[0], data[1], data[2])
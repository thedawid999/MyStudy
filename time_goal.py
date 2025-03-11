from goal import Goal

class TimeGoal(Goal):
    def __init__(self, title, startdate, deadline):
        super().__init__(title)
        self._startdate = startdate
        self._deadline = deadline

    def get_startdate(self):
        return self._startdate

    def get_deadline(self):
        return self._deadline

    def calculate_remaining_time(self):
        return None
        #define method!

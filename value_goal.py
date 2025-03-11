from goal import Goal

class ValueGoal(Goal):
    def __init__(self, title, value):
        super().__init__(title)
        self._value = value

    def get_title(self):
        return self._title

    def get_value(self):
        return self._value

    def calculate_average(self):
        return None

    def calculate_min_grade(self):
        return None
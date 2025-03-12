from goal import Goal

class ValueGoal(Goal):
    def __init__(self, title:str, value:float):
        super().__init__(title)
        self._value = value

    def get_title(self):
        return self._title

    def get_value(self):
        return self._value

    @staticmethod
    def calculate_average(self):
        # TODO: define method!
        return None

    @staticmethod
    def calculate_min_grade(self):
        # TODO: define method!
        return None
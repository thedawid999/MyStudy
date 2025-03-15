from goal import Goal
from student import Student

class ValueGoal(Goal):
    def __init__(self, title:str, value:float):
        super().__init__(title)
        self._value = value

    def get_title(self):
        return self._title

    def get_value(self):
        return self._value

    @staticmethod
    def calculate_average(self, student:Student):
        grades = ValueGoal.__extract_grades(self, student)
        avg = sum(grades) / len(grades)
        return avg

    @staticmethod
    def calculate_min_grade(self, student:Student):
        grades = ValueGoal.__extract_grades(self, student)
        courses = student.get_courses()

        minimum = (self._value*len(courses)-sum(grades))/(len(courses)-len(grades))
        return minimum

    @staticmethod
    def __extract_grades(self, student:Student):
        grades = []
        for course in student.get_courses():
            if course.grade != 0:
                grades.append(course.grade)
        return grades

    @staticmethod
    def to_valuegoal(data):
        return ValueGoal(data[1], data[2])
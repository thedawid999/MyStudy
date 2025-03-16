from typing import TYPE_CHECKING
from goal import Goal
if TYPE_CHECKING:
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
    def calculate_average(student: "Student"):
        grades = ValueGoal.__extract_grades(student)
        if len(grades) == 0:
            return 0.0
        avg = sum(grades) / len(grades)
        return avg

    def calculate_min_grade(self, student: "Student"):
        grades = ValueGoal.__extract_grades(student)
        courses = student.get_courses()

        minimum = (self._value*len(courses)-sum(grades))/(len(courses)-len(grades))
        return minimum

    @staticmethod
    def __extract_grades(student:"Student"):
        grades = []
        for course in student.get_courses():
            if course.get_grade() != 0:
                grades.append(course.get_grade())
        return grades

    @staticmethod
    def to_valuegoal(data):
        return ValueGoal(data[0], data[1])
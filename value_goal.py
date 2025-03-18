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
        """returns the average of all grades"""
        grades = ValueGoal.__extract_grades(student)
        if len(grades) == 0:
            return 0.0
        avg = sum(grades) / len(grades)
        return avg

    @staticmethod
    def calculate_min_grade(student: "Student"):
        """calculates the minimum grade the student needs to achieve in order to complete the value goal"""
        grades = ValueGoal.__extract_grades(student)
        courses = student.get_courses()
        value = 0

        for goal in student.get_goals():
            if isinstance(goal, ValueGoal):
                value = goal.get_value()
        try:
            minimum = (value*len(courses)-sum(grades))/(len(courses)-len(grades))
        except ZeroDivisionError:
            return 0
        return minimum

    @staticmethod
    def __extract_grades(student:"Student"):
        """returns only grades from courses list"""
        grades = []
        for course in student.get_courses():
            if course.get_grade() != 0:
                grades.append(course.get_grade())
        return grades

    @staticmethod
    def to_valuegoal(data):
        """converts db-data into a ValueGoal object"""
        return ValueGoal(data[0], data[1])
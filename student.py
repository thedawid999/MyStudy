from database import Database
from goal import Goal
from course import Course

class Student:
    def __init__(self, courses: list[Course], goals: list[Goal], db: Database):
        self._courses = courses
        self._goals = goals
        self._db = db
        #IN CASE DATABASE HAS DATA, IMPORT THEM FROM DATABASE

    def get_courses(self):
        return self._courses

    def get_goals(self):
        return self._goals

    def add_course(self, course: Course):
        #define method!
        return None

    def delete_course(self, course: Course):
        #define method!
        return None

    def delete_all_courses(self):
        #define method!
        return None

    def add_goal(self, goal: Goal):
        #define method!
        return None

    def delete_goal(self, goal: Goal):
        #define method!
        return None

    def calculate_finished_courses(self):
        #define method!
        return None

    def delete_student(self):
        #define method!
        return None


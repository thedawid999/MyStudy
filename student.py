from database import Database
from goal import Goal
from course import Course
from time_goal import TimeGoal
from value_goal import ValueGoal
from datetime import date


class Student:
    def __init__(self, courses: list[Course], goals: list[Goal], db: Database):
        self._courses = courses
        self._goals = goals
        self._db = db
        #IN CASE DATABASE HAS DATA, IMPORT THEM FROM DATABASE

    def get_courses(self):
        """returns the list of courses from object"""
        return self._courses

    def get_goals(self):
        """returns the list of goals from object"""
        return self._goals

    def read_courses(self):
        """returns courses from database, will be used for data loading at the beginning"""
        return self._db.get_courses()

    def read_goals(self):
        """returns goals from database, will be used for data loading at the beginning"""
        return self._db.get_value_goals() + self._db.get_time_goals()

    def add_course(self, *args):
        """
        if there is 1 args it is considered as title
            - adds Course to course list (grade has a default value of 0)
            - adds Course to database (grade has a default value of 0)
        if there are 2 args it is considered as title and grade
            - adds Course to course list
            - add Course to database
        :param args: title OR title, value
        :return: none
        """
        try:
            if len(args) == 1:
                self._courses.append(Course(args[0], self._db))
                self._db.add_course(Course(args[0], self._db))
            elif len(args) == 2:
                if 1 <= float(args[1]) <= 6:
                    self._courses.append(Course(args[0], self._db, float(args[1])))
                    self._db.add_course(Course(args[0], self._db, float(args[1])))
                else:
                    raise ValueError
        except ValueError:
            print("correct format of course is TITLE (str) [GRADE (float between 1 and 6)]")

    def delete_course(self, *args):
        """
        checks if given course name exists in course list
            - if exists the course will be removed from _courses and from the database
        :param args: course name
        :return: none
        """
        for course in self._courses:
            if args[0] == course.get_name():
                self._courses.remove(course)
                self._db.delete_course(course)

    def add_goal(self, *args):
        """
        if there are 2 args, it is considered a ValueGoal
            - checks if the second argument can be converted to float
            - checks if the second argument is a number between 1 and 6
            - adds it to _goals and to database
            - else: raise ValueError
        if there are 3 args, it is considered a TimeGoal
            - checks if the second and third argument can be converted to date
            - checks if second argument is an earlier date than the second argument
            - adds it to _goals and to database
            - else: raise ValueError
        :param args: title, value OR title, startdate, deadline
        :return: none
        """
        try:
            if len(args) == 2:
                if 1 <= float(args[1]) <= 6:
                    self._goals.append(ValueGoal(args[0], float(args[1])))
                    self._db.add_goal(ValueGoal(args[0], float(args[1])))
                else:
                    raise ValueError
            elif len(args) == 3:
                if date.fromisoformat(args[1]) < date.fromisoformat(args[2]):
                    self._goals.append(TimeGoal(args[0], args[1], args[2]))
                    self._db.add_goal(TimeGoal(args[0], args[1], args[2]))
                else:
                    raise ValueError
        except ValueError:
            print("correct format of value goal is TITLE (str) VALUE (float between 1 and 6)")
            print("correct format of time goal is TITLE (str) STARTDATE (yyyymmdd) DEADLINE (yyyymmdd)")


    def delete_goal(self, *args):
        """
        checks if given title exists in goals list
            - if exists, the goal will be removed from _goals and from the database
        :param args: title
        :return: none
        """
        for goal in self._goals:
            if args[0] == goal.get_title():
                self._goals.remove(goal)
                self._db.delete_goal(goal)
        else:
            print("this goal does not exist!")

    def calculate_finished_courses(self):
        #define method!
        return None

    def delete_student(self):
        #define method!
        return None


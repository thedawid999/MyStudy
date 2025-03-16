from typing import TYPE_CHECKING
from datetime import date
from event_handler import EventHandler
from event import Event
from course import Course
from time_goal import TimeGoal
from value_goal import ValueGoal
from rich import print
if TYPE_CHECKING:
    from database import Database

MAX_TIME_GOALS = 3
MAX_VALUE_GOALS = 1

class Student:
    def __init__(self, db: "Database"):
        self._db = db
        self._courses = []
        self._goals = []

        if not db.is_table_empty("courses"):
            data = db.get_courses()
            for d in data:
                self._courses.append(Course.to_course(d, db))
        if not db.is_table_empty("timegoals"):
            data = db.get_time_goals()
            for d in data:
                self._goals.append(TimeGoal.to_timegoal(d))
        if not db.is_table_empty("valuegoals"):
            data = db.get_value_goals()
            self._goals.append(ValueGoal.to_valuegoal(data[0]))

        EventHandler.subscribe(Event.ADD_GOAL, self.add_goal)
        EventHandler.subscribe(Event.DELETE_GOAL, self.delete_goal)
        EventHandler.subscribe(Event.ADD_GRADE, self.add_grade)
        EventHandler.subscribe(Event.DELETE_GRADE, self.delete_grade)
        EventHandler.subscribe(Event.ADD_COURSE, self.add_course)
        EventHandler.subscribe(Event.DELETE_COURSE, self.delete_course)
        EventHandler.subscribe(Event.DELETE_STUDENT, self.delete_student)

    def get_courses(self):
        """returns the list of courses from object"""
        return self._courses

    def get_goals(self):
        """returns the list of goals from object"""
        return self._goals

    def add_course(self, args):
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
            print("[red italic]--> correct format of course is TITLE (str) [GRADE (float between 1 and 6)][/]")

    def delete_course(self, args):
        """
        checks if given course name exists in course list
            - if exists the course will be removed from _courses and from the database
        :param args: course name
        :return: none
        """
        if len(args) == 0:
            print("[red italic]--> correct format of delcourse is COURSENAME (str)")
        for course in self._courses:
            if args[0] == course.get_name():
                self._courses.remove(course)
                self._db.delete_course(course)
                return
        print("[red italic]--> course does not exist!")

    def add_goal(self, args):
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
        verifies the amount of TimeGoals and ValueGoals, already exisiting (TimeGoal max. 3, ValueGoal max. 1)
        :param args: title, value OR title, startdate, deadline
        :return: none
        """

        try:
            if len(args) == 2:
                if sum(1 for goal in self._goals if isinstance(goal, ValueGoal)) == MAX_VALUE_GOALS:
                    raise OverflowError
                if 1 <= float(args[1]) <= 6:
                    self._goals.append(ValueGoal(args[0], float(args[1])))
                    self._db.add_goal(ValueGoal(args[0], float(args[1])))
                else:
                    raise ValueError
            elif len(args) == 3:
                if sum(1 for goal in self._goals if isinstance(goal, TimeGoal)) == MAX_TIME_GOALS:
                    raise OverflowError
                if date.fromisoformat(args[1].strip()) < date.fromisoformat(args[2].strip()):
                    self._goals.append(TimeGoal(args[0], args[1], args[2]))
                    self._db.add_goal(TimeGoal(args[0], args[1], args[2]))
                else:

                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("[red italic]--> correct format of value goal is TITLE (str) VALUE (float between 1 and 6)")
            print("[red italic]--> correct format of time goal is TITLE (str) STARTDATE (yyyy-mm-dd) DEADLINE (yyyy-mm-dd)")
        except OverflowError:
            print(f"[red italic]--> maximal amount of TimeGoals is {MAX_TIME_GOALS}, maximal amount of ValueGoals is {MAX_VALUE_GOALS}")


    def delete_goal(self, args):
        """
        checks if given title exists in goals list
            - if exists, the goal will be removed from _goals and from the database
        :param args: title
        :return: none
        """
        if len(args) == 0:
            print("[red italic]--> correct format of delgoal is TITLE (str)")
        for goal in self._goals:
            if args[0] == goal.get_title():
                self._goals.remove(goal)
                self._db.delete_goal(goal)
                return
        print("[red italic]--> this goal does not exist!")

    def add_grade(self, args):
        """
        - checks if given course name exists in course list
        - check if second argument is between 1 and 6
        if so, the rest of the logic continues in Course-class
        :param args: course name, grade
        :return:
        """
        try:
            if 1 > float(args[1]) < 6:
                raise ValueError
            for course in self._courses:
                if course.get_name() == args[0]:
                    course.add_grade(float(args[1]))
                    return
            print("[red italic]--> course does not exist!")
        except ValueError:
            print("[red italic]--> correct format of addgrade is COURSE NAME (str) GRADE (float between 1 and 6)")

    def delete_grade(self, args):
        """
        - checks if given course name exists in course list
        if so, the rest of the logic continues in Course-class
        :param args: course name
        :return:
        """
        if len(args) == 0:
            print("[red italic]--> correct format of delgrade is COURSENAME (str)")
        for course in self._courses:
            if args[0] == course.get_name():
                course.delete_grade()
                return
        print("[red italic]--> course does not exist!")

    def calculate_finished_courses(self):
        finished = 0
        for course in self._courses:
            if course.get_grade() != 0:
                finished += 1
        return finished

    def delete_student(self, args):
        self._db.delete_student()
        exit()



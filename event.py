from enum import Enum

class Event(Enum):
    ADD_COURSE = "add_course"
    DELETE_COURSE = "delete_course"
    ADD_GOAL ="add_goal"
    DELETE_GOAL = "delete_goal"
    ADD_GRADE = "add_grade"
    DELETE_GRADE = "delete_grade"
    DELETE_STUDENT = "delete_student"
    SHOW_GRADES = "show_grades"
    SHOW_DASHBOARD = "show_dashboard"


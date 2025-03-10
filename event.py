from enum import Enum

class Event(Enum):
    #student events
    GET_STUDENT_NAME = "get_student_name"
    GET_COURSES = "get_courses"
    GET_GOALS = "get_goals"
    ADD_COURSE = "add_course"
    DELETE_COURSE = "delete_course"
    DELETE_ALL_COURSES = "delete_all_courses"
    ADD_GOAL ="add_goal"
    DELETE_GOAL = "delete_goal"
    CALCULATE_FINISHED_COURSES = "calculate_finished_courses"
    DELETE_STUDENT = "delete_student"

    #course events
    GET_COURSE_NAME = "get_course_name"
    GET_GRADE = "get_grade"
    ADD_GRADE = "add_grade"
    DELETE_GRADE = "delete_grade"


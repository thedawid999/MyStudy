from student import Student

class Visualizer:
    _student = None
    @staticmethod
    def set_student(student: Student):
        Visualizer._student = student

    @staticmethod
    def show_dashboard():
        #TODO: define method!
        return None

    @staticmethod
    def show_grades():
        #TODO: define method!
        return None

    @staticmethod
    def show_help():
        #TODO: define method!
        """
        Usage: my_program [OPTIONS] COMMAND [ARGS]...

        A simple program to manage courses and goals.

        Options:
          -h, --help       Show this message and exit.

        Commands:
          add_course NAME GRADE     Add a course with a grade.
          delete_course NAME        Remove a course by name.
          add_time_goal TITLE START DEADLINE
                                    Add a time goal with a title, start date, and deadline.
          delete_time_goal TITLE    Remove a time goal by title.
          add_value_goal TITLE VALUE
                                    Add a value goal with a title and value.
          delete_value_goal TITLE   Remove a value goal by title.
          get_courses               List all courses with grades.
          get_time_goals            List all time goals.
          get_value_goals           List all value goals.

        Examples:
          my_program add_course "Math" 4.0
          my_program add_time_goal "Project" "2025-03-11" "2025-06-01"
          my_program get_courses
        :return:
        """

        return None
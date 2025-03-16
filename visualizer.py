from rich.align import Align
from rich.progress import Progress, TextColumn, BarColumn
from student import Student
from time_goal import TimeGoal
from value_goal import ValueGoal
from rich.padding import Padding
from rich import print
from rich.panel import Panel
from rich.console import Group, Console
from rich.text import Text
from rich.table import Table

class Visualizer:
    _student: Student = None
    _deadline_progress_bars = []
    _deadline_panel = None
    _progress_bar = None
    _grades_panel = None
    _layout = None

    @staticmethod
    def __create_progress_bars():
        """creates progress bars for timegoals and for value goal"""
        student = Visualizer._student
        Visualizer._deadline_progress_bars = []

        #deadlines
        for goal in student.get_goals():
            if isinstance(goal, TimeGoal):
                progress = Progress(
                    BarColumn(complete_style="bold red", finished_style="bold green", pulse_style="bold", bar_width=200),
                    TextColumn("[white]{task.percentage:>3.0f}%", justify="right"),  # Remove time
                    expand=True,
                )
                task = progress.add_task(goal.get_title(), total=100)

                progress.update(task, completed=goal.calculate_remaining_time_percentage())

                days_left = goal.calculate_days_left()
                progressbar = Group(
                    Text.from_markup(f"[bold blue]{goal.get_title()}[/] | [italic purple]{goal.get_startdate()} --> {goal.get_deadline()} [/]| "
                                     f"days left: {days_left}", justify="left"),
                    progress
                )
                Visualizer._deadline_progress_bars.append(progressbar)

        #course progress
        progress = Progress(
            BarColumn(complete_style="bold red", finished_style="bold green", pulse_style="bold", bar_width=200),
            # Set custom width
            TextColumn("[white]{task.percentage:>3.0f}%", justify="right"),  # Remove time
            expand=True,
        )
        task = progress.add_task("", total=len(Visualizer._student.get_courses()))

        progress.update(task, completed=Visualizer._student.calculate_finished_courses())
        Visualizer._progress_bar = progress

    @staticmethod
    def __deadlines_panel():
        """creates a panel for deadlines"""
        return Padding(Panel(Group(*Visualizer._deadline_progress_bars), title="Deadlines"), (1,3,0,3))

    @staticmethod
    def __progress_panel():
        """creates a panel for progress"""
        student = Visualizer._student
        courses = len(student.get_courses())
        finished_courses = student.calculate_finished_courses()

        if Visualizer._progress_bar is not None:
            return Padding(Panel(Group(Text(f"courses finished: {finished_courses}/{courses}"), Visualizer._progress_bar), title="Progress"), (1,3,0,3))
        else:
            return Padding(Panel(Text("no courses yet"), title="Progress"),(1,3,0,3))

    @staticmethod
    def __grades_panel():
        """creates a panel for grades"""
        student = Visualizer._student
        avg = ValueGoal.calculate_average(student)
        goal:ValueGoal = next(filter(lambda g: isinstance(g, ValueGoal), student.get_goals()), None)
        goal_value = goal.get_value() if goal else "no goal set"
        goal_title = goal.get_title() if goal else ""

        return Padding(Panel(Group(Text(f"Average: {avg}"), Text(f"Goal: {goal_value} ({goal_title})")), title="Grades"), (1,3,0,3))

    @staticmethod
    def set_student(student: Student):
        Visualizer._student = student

    @staticmethod
    def show_dashboard():
        """displays main dashboard"""
        title = Text("MY STUDY DASHBOARD", justify="center", style="bold red")
        print(Align(title, align="center"))

        Visualizer.__create_progress_bars()
        layout = Group(Visualizer.__deadlines_panel(), Visualizer.__progress_panel(), Visualizer.__grades_panel())
        print(layout)

    @staticmethod
    def show_grades():
        """displays all grades"""
        title = Text("MY GRADES", justify="center", style="bold red")
        title.append(" (to achieve Goal)", style="yellow")
        min_grade = 0

        student = Visualizer._student
        courses = student.get_courses()

        if not courses:
            print("[bold red]No courses available.[/]")

        table = Table(border_style="grey54", show_lines=True)

        # Define 3 columns
        table.add_column("Course", justify="left", style="white")
        table.add_column("Grade", justify="center", style="yellow")
        table.add_column("Status", justify="right", style="bold green")

        for goal in student.get_goals():
            if isinstance(goal, ValueGoal):
                min_grade = ValueGoal.calculate_min_grade(student)

        for course in courses:
            grade = course.get_grade()
            status = "Passed" if grade and grade <= 4.0 else "Failed" if grade else "Pending..."
            status_style = "bold green" if status == "Passed" else "bold red" if status == "Failed" else "dark_orange"

            table.add_row(course.get_name(), Visualizer.get_grade(grade, min_grade),f"[{status_style}]{status}[/]")

        print(Align(title, align="center"))
        print(Align(table, align="center"))

    @staticmethod
    def get_grade(grade, min_grade):
        if grade != 0:
            return f"{grade}"
        elif min_grade !=0:
            return f"N/A [bold yellow]({min_grade:.1f})[/]"
        else:
            return "N/A"

    @staticmethod
    def show_help():
        """displays all commands"""
        console = Console()

        help_text = Text()
        help_text.append("\nA simple program to manage your courses, grades, and goals\n\n", style="bold cyan")

        help_text.append("Usage: ", style="bold white")
        help_text.append("[ ", style="white")
        help_text.append("COMMAND", style="italic yellow")
        help_text.append(" ] [ ", style="white")
        help_text.append("ARGS", style="italic magenta")
        help_text.append(" ]\n\n", style="white")

        help_text.append("Commands:\n", style="bold underline blue")

        commands = [
            ("addcourse", "NAME", "Add a course only."),
            ("addcourse", "NAME GRADE", "Add a course with a grade."),
            ("delcourse", "NAME", "Remove a course by name."),
            ("addgrade", "COURSENAME GRADE", "Add a grade to an existing course."),
            ("delgrade", "COURSENAME", "Remove a grade from an existing course."),
            ("addgoal", "TITLE STARTDATE DEADLINE", "Add a time goal (YYYY-MM-DD format)."),
            ("addgoal", "TITLE VALUE", "Add a value goal."),
            ("delgoal", "TITLE", "Remove a goal by title."),
            ("help", " ", "Display all commands."),
            ("showgrades", " ", "Display all courses and grades."),
            ("dashboard", " ", "Display dashboard (main screen)."),
            ("exit", " ", "Exit the program."),
        ]

        for command, args, description in commands:
            help_text.append(f"  {command:13}", style="bold yellow")
            if args:
                help_text.append(f"{args:<28}", style="italic magenta")
            help_text.append(f"{description}\n", style="white")

        help_text.append("\nExamples:\n", style="bold underline blue")

        examples = [
            ("addcourse", "Mathematik:Analysis 2.1"),
            ("addgrade", "Informatik 3.0"),
            ("addgoal", "ProjektX 20250101 20250601"),
            ("addgoal", "Notenschnitt 1.5"),
        ]

        for command, example in examples:
            help_text.append(f"  {command} ", style="bold yellow")
            help_text.append(f"{example}\n", style="italic magenta")

        console.print(Panel(help_text, title="Help", border_style="bright_blue"))

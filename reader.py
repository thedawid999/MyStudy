from event_handler import EventHandler
from visualizer import Visualizer
from event import Event

class Reader:
    @staticmethod
    def read_input():
        user_input = input("your input: ").lower().split()

        command = user_input[0]
        args = user_input[1:]

        match command:
            case "help":
                Visualizer.show_help()
            case "addgoal":
                EventHandler.publish(Event.ADD_GOAL, args)
                Visualizer.show_dashboard()
            case "delgoal":
                EventHandler.publish(Event.DELETE_GOAL, args)
                Visualizer.show_dashboard()
            case "addgrade":
                EventHandler.publish(Event.ADD_GRADE, args)
                Visualizer.show_dashboard()
            case "delgrade":
                EventHandler.publish(Event.DELETE_GRADE, args)
                Visualizer.show_dashboard()
            case "addcourse":
                EventHandler.publish(Event.ADD_COURSE, args)
                Visualizer.show_dashboard()
            case "delcourse":
                EventHandler.publish(Event.DELETE_COURSE, args)
                Visualizer.show_dashboard()
            case "delstudent":
                EventHandler.publish(Event.DELETE_STUDENT, None)
                exit()
            case "showgrades":
                Visualizer.show_grades()
            case "dashboard":
                Visualizer.show_dashboard()
            case "exit":
                exit()

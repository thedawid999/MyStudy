class Reader:
    @staticmethod
    def read_input():
        user_input = input("your input: ").lower().split()

        command = user_input[0]
        args = user_input[1:]

        match command:
            case "help":
                print("help")
                #call visualizer directly
            case "addgoal":
                if len(args) == 2:
                    print("value goal")
                elif len(args) == 3:
                    print("timegoal goal")
                else:
                    print("wrong input")
            case "delgoal":
                if len(args) == 1:
                    print("deleted")
                else:
                    print("wrong input")
            case "addgrade":
                if len(args) == 2:
                    print("grade added")
                else:
                    print("wrong input")
            case "delgrade":
                if len(args) == 1:
                    print("grade deleted")
                else:
                    print("wrong input")
            case "addcourse":
                if len(args) == 1:
                    print("course added")
                elif len(args) == 2:
                    print("course and grade added")
                else:
                    print("wrong input")
            case "delcourse":
                if len(args) == 1:
                    print("course deleted")
                else:
                    print("wrong input")
            case "delstudent":
                print("del student")
            case "showgrades":
                print("show grades")
                # call visualizer directly
            case "dashboard":
                print("dashboard")
                # call visualizer directly
            case "exit":
                exit()

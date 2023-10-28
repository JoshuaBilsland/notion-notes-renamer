class Renamer:
    def __init__(self):
        print("--------------------")
        print("notion-notes-renamer")
        print("--------------------\n")

        print(self.__display_menu())
        user_input = self.__get_input()
        self.__handle_input(user_input)

    def __display_menu(self):
        print("Menu Options")
        print("------------")
        print("f - rename a singular file")
        print("d - rename all the files within a given directory")
        print("\nUse 'help <command>' to get more information about a command")

    def __get_input(self):
        return input("\n>> ")

    def __handle_input(self, user_input):
        split_input = user_input.split(" ")
        if len(split_input) == 2:
            if split_input[0] == "f":
                print()
            elif split_input[0] == "d":
                print()  # handle d
            elif split_input[0] == "help":
                print()  # handle help
            else:
                print(f"ERROR: {split_input[0]} is not a menu option")
        else:
            print("ERROR: Invalid command. Try using 'help <command>'")

    def __file_exists(self, file_path):
        try:
            file = open(file_path, "r")
        except FileNotFoundError:
            return False
        else:
            file.close()
            return True


if __name__ == "__main__":
    Renamer()

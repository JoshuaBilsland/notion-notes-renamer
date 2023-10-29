import os
import datetime
import help


class Renamer:
    def __init__(self):
        print("--------------------")
        print("notion-notes-renamer")
        print("--------------------\n")

        self.__main_loop()

    def __main_loop(self):
        self.__display_menu()
        running = True
        while running:
            user_input = self.__get_input()
            handled_input = self.__handle_input(user_input)
            if handled_input == "quit":
                running = False

    def __display_menu(self):
        print("Menu Options")
        print("------------")
        print("f - rename a singular file")
        print("d - rename all the files within a given directory")
        print("\nq - close the program")
        print("\nUse 'help <command>' to get more information about a command")

    def __get_input(self):
        return input("\n>> ")

    def __handle_input(self, user_input):
        if user_input == "q":
            return "quit"

        split_input = user_input.split(" ")
        if len(split_input) == 2:
            # Make into a raw string for open() to work
            split_input[1] = rf"{split_input[1]}"

            if split_input[0] == "f":
                self.__handle_f(split_input[1])
            elif split_input[0] == "d":
                self.__handle_d(split_input[1])  # Handle d
            elif split_input[0] == "help":
                print(help.handle_help(split_input))  # Handle help
            else:
                print(f"ERROR: {split_input[0]} is not a menu option")
        else:
            print("ERROR: Invalid command. Try using 'help <command>'")

    def __handle_f(self, file_path):
        if self.__file_exists(file_path):
            # Join the original path with the new file name
            path, old_name = os.path.split(file_path)
            new_name = self.__rename_file(old_name)
            new_file_path = os.path.join(path, new_name)
            os.rename(file_path, new_file_path)
        else:
            print("ERROR: File does not exist")

    def __handle_d(self, dir_path):
        if self.__dir_exists(dir_path):
            files_list = os.listdir(dir_path)
            for file in files_list:
                new_name = self.__rename_file(file)
                old_file_path = os.path.join(dir_path, file)
                new_file_path = os.path.join(dir_path, new_name)
                os.rename(old_file_path, new_file_path)
        else:
            print("ERROR: Directory does not exist")

    def __file_exists(self, file_path):
        try:
            file = open(file_path, "r")
        except FileNotFoundError:
            return False
        else:
            file.close()
            return True

    def __dir_exists(self, dir_path):
        return os.path.isdir(dir_path)

    def __rename_file(self, file_name):
        # EXAMPLE: 0fd35cb5-381e-4e8c-966c-897310c6095a_Mastering_Python_-_Everything_You_Need_To_Know_To_Become_a_Python_Master

        first_underscore = file_name.find("_")

        # Remove the start (0fd35...95a part)
        removed_start = file_name[first_underscore:]

        # Make all letters lowercase
        lowered = removed_start.lower()

        # Prepend the date
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%Y-%m-%d")

        return formatted_date + lowered


if __name__ == "__main__":
    Renamer()

def handle_help(self, split_input):
    if split_input[1] == "f":
        return_value = get_f_command_help()
    elif split_input[1] == "d":
        return_value get_d_command_help()
    else:
        return_value = f"ERROR: No help for {split_input[1]}"
    return return_value

def get_f_command_help():
    return """Rename a singular file by providing the path to it.

To use this command, enter 'f' followed by the path to the file

The path should be given as the plain path.

Example: f F:\test_folder
    """
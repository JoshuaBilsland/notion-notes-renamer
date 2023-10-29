def handle_help(split_input):
    if split_input[1] == "f":
        return_value = get_f_command_help()
    elif split_input[1] == "d":
        return_value = get_d_command_help()
    else:
        return_value = f"ERROR: No help for {split_input[1]}"
    return return_value


def get_f_command_help():
    return r"""Rename a singular file by providing the path to it.

To use this command, enter 'f' followed by the path to the file.

The path should be given as the plain path.

Example: f F:\test_folder\0fd35cb5-381e-4e8c-966c-897310c6095a_Mastering_Python_-_Everything_You_Need_To_Know_To_Become_a_Python_Master.pdf
    """


def get_d_command_help():
    return r"""Rename all the files within a directory.

To use this command, enter 'd' followed by the path to the directory.

The path should be given as the plain path.

Note: Ensure that the directory only contains files that need to be renamed.

Example: d F:\test_folder
"""

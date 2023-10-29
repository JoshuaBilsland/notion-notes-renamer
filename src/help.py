def handle_help(self, split_input):
    if split_input[1] == "f":
        return_value = get_f_command_help()
    elif split_input[1] == "d":
        return_value get_d_command_help()
    else:
        return_value = f"ERROR: No help for {split_input[1]}"
    return return_value
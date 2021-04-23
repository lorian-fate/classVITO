from manage import Manage_Bets


def my_main():
    exit_command = True
    my_obj = Manage_Bets()
    my_obj.head()
    while exit_command:
        command_line = input(">>>> ")
        keyword_list = command_line.split(" ")
        if len(keyword_list) == 1: 
            if command_line.lower() == 'exit':
                exit_command = False
            else:
                my_obj.solo_command(command_line)
        elif keyword_list[1].lower() == 'help': my_obj.help_command(keyword_list)
        elif keyword_list[0].lower() == 'show': my_obj.show_command(keyword_list)
        elif keyword_list[0].lower() == 'makebet': my_obj.makebet_command(keyword_list)

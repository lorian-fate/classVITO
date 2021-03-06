import math
import json
from datetime import datetime


"""
    #! al prescindir del valor más alto te arriegas a perder la apuesta
    #! si el resultado del partido corresponde al valor del valor prescindido,
    #! No obstante esta perdida se puede recuperar si solo se pierden dos o 
    #! menos apuestas no más
"""

class My_Bet_APP:
    detail_command = {
        'makebet': {
            '+league_name': "type a league's name", 
            '+name_first_team': "type the first team's name",
            '+name_second_team': "type the second team's name",
            '+profit_local': "type the profit correspondent to the local team",
            '+profit_draw': "type the profit correspondent to a draw",
            '+profit_visitor': "type the profit correspondent to the visitor team",
            '+amount_to_bet':"type the amount to bet. Is an optional option",
            'e.g':"makebet league_name local_team visitor_team profit_local profit_draw profit_visitro amount_to_bet"
            },
        'show': {
            "+recommended bets": "show all recommended bets saved",
            "+dangerous bets": "show the last five bet tried",
            "+all bets": "show bets's history"
            }
    }
    command_list = {
        'listcommand': 'show all allowed commands',
        'makebet':'allow make a new bet',
        'exit': 'exits the program',
        'show': 'take more argument and show that the argument ask',
        'help': "goes after a command and show how use a command in detail. e.g 'makebet help'",
        'clean': "clean your screen"

        }

    def __init__(self, league=None, team_tuple=None, local_winer=None, 
    draw=None, visitor_winer=None, amount_to_bet=10):
        self.team_tuple = team_tuple
        self.local_winer = local_winer
        self.visitor_winer = visitor_winer
        self.draw = draw
        self.league = league
        self.amount_to_bet = int(amount_to_bet)


    
    def save_Data(self, file_name):
        directory = f"./BETS_DATAS/{file_name}.json"
        my_file = open(directory)
        my_data = json.load(my_file)
        my_file.close()
        my_dictionary = {
                    'league': self.league,
                    'date': datetime.today().strftime("%d-%m-%Y"),
                    'local_team': self.team_tuple[0],
                    'visitor_team': self.team_tuple[1],
                    'local_winer': self.local_winer,
                    'visitor_winer': self.visitor_winer,
                    'draw': self.draw
        }
        if my_dictionary not in my_data["data"]:
            my_data["data"].append(my_dictionary)
            with open(directory, "w") as json_File:
                json.dump(my_data, json_File, indent=4)



    @property
    def my_Validator(self):
        x = 0
        for i in range(self.amount_to_bet*100):
            x += 0.01
            y = self.amount_to_bet - x
            my_tuple = (round(x, 2), round(y, 2))
            yield my_tuple


    def amount_calculation(self, value_list, message, my_obj, json_name):
        my_obj.save_Data("historical_Bets")
        value_to_use = []
        value_to_use.insert(0, value_list.pop(value_list.index(min(value_list))))
        value_to_use.insert(0, value_list.pop(value_list.index(min(value_list))))
        value1 = value_to_use[0]
        value2 = value_to_use[1]
        for my_tuple in list(self.my_Validator):
            if (my_tuple[0]*value1 > self.amount_to_bet) and (my_tuple[1]*value2 > self.amount_to_bet):
                my_profit1 = (my_tuple[0]*value1) - self.amount_to_bet
                my_profit2 = (my_tuple[1]*value2) - self.amount_to_bet
                my_sustraction = round((my_profit2 - my_profit1), 3)
                if -0.035 <= my_sustraction <= 0.035:
                    my_obj.save_Data(json_name)
                    print(f"bet {my_tuple[0]} to {value1} and your profit will be {round(my_profit1, 2)}\
                            \nbet {my_tuple[1]} to {value2} and your profit will be {round(my_profit2, 2)}\
                            \nNote:{message}")


    def my_BETS(self):
        my_obj = My_Bet_APP(self.league, self.team_tuple, self.local_winer, 
                        self.visitor_winer, self.draw, self.amount_to_bet )
        value_list = [float(self.local_winer), float(self.visitor_winer), float(self.draw)]
        validation = ((max(value_list)*100)/sum(value_list))/100
        
        if validation >= 0.55:
            mess = "Bet recommended"
            my_obj.amount_calculation(value_list, mess, my_obj, "recomended_Bets")

        elif 0.40 <= validation <= 0.55:
            mess = "Dangerous Bet"
            my_obj.amount_calculation(value_list, mess, my_obj, "dangerous_Bets")
        else:
            my_obj.save_Data("historical_Bets")
            print("Bet not recommended")


"""
def main():
    exit_command = True
    detail_command = My_Bet_APP.detail_command 
    command_list = My_Bet_APP.command_list

    print("=================================================================")
    print("================== WELCOME TO YOUR BET APP ======================")
    print("=================================================================")
    print("Type 'listcommand' to show allowed commands or 'help' ")
    while exit_command:
        command_line = input(">>>> ")
        keyword_list = command_line.split(" ")
        if len(keyword_list) == 1:
            if command_line.lower() == 'exit':
                exit_command = False
            elif command_line.lower() == 'clean':
                system("cls")
            elif command_line.lower() == 'listcommand' or command_line.lower() == 'help':
                for command, utility in command_list.items():
                    if len(command) <= 6:
                        print(command.upper(),"\t\t",utility)
                    else:
                        print(command.upper(),"\t",utility)
            elif command_line.lower() in detail_command.keys():
                print(f"The command '{command_line}' need more parameters. Type it with 'help' to more information")
            else:
                print(f"'{command_line}' isn't a inner command of this program")
        else:
            if keyword_list[1].lower() == 'help':
                if len(keyword_list) == 2:
                    if keyword_list[0] in detail_command.keys():
                        print(F"so you can use '{keyword_list[0]}'")
                        for my_command, utility in detail_command[keyword_list[0]].items():
                            if len(my_command) <= 14:
                                print(my_command.upper(), "\t\t", utility)
                            else:
                                print(my_command.upper(), "\t", utility)
                    else:
                        print(f"'{keyword_list[0]}' isn't a inner command of this program")
                else:
                    print("command error")

            else:
                if keyword_list[0].lower() == 'makebet':
                    if (len(keyword_list) == 8 or len(keyword_list) == 7) and (keyword_list[0] in detail_command.keys()):
                        if len(keyword_list) == 8:
                            obj = My_Bet(keyword_list[1], (keyword_list[2], keyword_list[3]), 
                            keyword_list[4], keyword_list[5], keyword_list[6], keyword_list[7])
                            if (type(float(keyword_list[4])) == float) and (type(float(keyword_list[6])) == float) \
                            and (type(float(keyword_list[6])) == float):
                                if keyword_list[0].lower() == 'makebet':
                                    obj.my_BETS()

                        elif len(keyword_list) == 7:
                            obj = My_Bet(keyword_list[1], (keyword_list[2], keyword_list[3]), 
                            keyword_list[4], keyword_list[5], keyword_list[6])
                            if (type(float(keyword_list[4])) == float) and (type(float(keyword_list[6])) == float) \
                            and (type(float(keyword_list[6])) == float):
                                if keyword_list[0].lower() == 'makebet':
                                    obj.my_BETS()
                    else:
                        print("missing arguments")

                elif keyword_list[0].lower() == 'show':
                    if (keyword_list[1].lower() == 'recommended') and (keyword_list[2].lower() == 'bets'):
                        with open("./BETS_DATAS/recomended_Bets.json") as my_File:
                            my_json = json.load(my_File)
                            print("DATE", "\t\t", "LOCAL TEAM", "\t\t", "VISITOR TEAM", "\t\t", "LOCAL WINER", "\t\t", 
                            "VISITOR WINER", "\t\t", "DRAW")
                            print("============================================================\
=========================================================")
                            for my_data in my_json["data"]:
                                if len(my_data["local_team"]) >= 14 and len(my_data["visitor_team"]) >= 14:
                                    print(my_data["date"], "\t", my_data["local_team"], "\t", my_data["visitor_team"], 
                                    "\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                                elif len(my_data["local_team"]) >= 14:
                                    print(my_data["date"], "\t", my_data["local_team"], "\t", my_data["visitor_team"], 
                                    "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                                elif len(my_data["visitor_team"]) >= 14:
                                    print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                    "\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                                else:
                                    print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                    "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    
                    elif keyword_list[1].lower() == 'previous':
                        pass
                    elif keyword_list[1].lower() == 'all':
                        pass

main()


"""








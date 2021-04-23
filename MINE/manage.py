from bets import My_Bet_APP
from os import system
import json

class Manage_Bets:
    detail_command = My_Bet_APP.detail_command 
    command_list = My_Bet_APP.command_list


    def head(self):
        print("=================================================================")
        print("================== WELCOME TO YOUR BET APP ======================")
        print("=================================================================")
        print("Type 'listcommand' to show allowed commands or 'help' ")


    def makebet_command(self, keyword_list):
        if (len(keyword_list) == 8 or len(keyword_list) == 7) and (keyword_list[0] in self.detail_command.keys()):
            if len(keyword_list) == 8:
                obj = My_Bet_APP(keyword_list[1], (keyword_list[2], keyword_list[3]), 
                keyword_list[4], keyword_list[5], keyword_list[6], keyword_list[7])
                if (type(float(keyword_list[4])) == float) and (type(float(keyword_list[6])) == float) \
                    and (type(float(keyword_list[6])) == float):
                    if keyword_list[0].lower() == 'makebet':
                        obj.my_BETS()

            elif len(keyword_list) == 7:
                obj = My_Bet_APP(keyword_list[1], (keyword_list[2], keyword_list[3]), 
                keyword_list[4], keyword_list[5], keyword_list[6])
                if (type(float(keyword_list[4])) == float) and (type(float(keyword_list[6])) == float) \
                    and (type(float(keyword_list[6])) == float):
                    if keyword_list[0].lower() == 'makebet':
                        obj.my_BETS()
        else:
            print("missing arguments")


    def help_command(self, keyword_list):
        if len(keyword_list) == 2:
            if keyword_list[0] in self.detail_command.keys():
                print(F"so you can use '{keyword_list[0]}'")
                for my_command, utility in self.detail_command[keyword_list[0]].items():
                    if 6 <= len(my_command) <= 14:
                        print(my_command.upper(), "\t\t", utility)
                    elif len(my_command) <= 6:
                        print(my_command.upper(), "\t\t\t", utility)
                    else:
                        print(my_command.upper(), "\t", utility)
            else:
                print(f"'{keyword_list[0]}' isn't a inner command of this program")
        else:
            print("command error")


    def show_command(self, keyword_list):
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

        elif (keyword_list[1].lower() == 'all') and (keyword_list[2].lower() == 'bets'):
            with open("./BETS_DATAS/historical_Bets.json") as my_File:
                my_json = json.load(my_File)
                print("DATE", "\t\t", "LOCAL TEAM", "\t\t", "VISITOR TEAM", "\t\t", "LOCAL WINER", "\t\t", 
                        "VISITOR WINER", "\t\t", "DRAW")
                print("============================================================\
=========================================================")
                for my_data in my_json["data"]:
                    
                    if len(my_data["local_team"]) < 6 and len(my_data["visitor_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["local_team"]) < 6 and len(my_data["visitor_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", my_data["visitor_team"], 
                                "\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["local_team"]) >= 14 and len(my_data["visitor_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["local_team"]) >= 14 and len(my_data["visitor_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])

                    elif len(my_data["local_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", my_data["visitor_team"], 
                                "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["visitor_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])

                    elif len(my_data["local_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t", my_data["visitor_team"], 
                                "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["visitor_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    else:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
        elif (keyword_list[1].lower() == 'dangerous')  and (keyword_list[2].lower() == 'bets'):
            with open("./BETS_DATAS/dangerous_Bets.json") as my_File:
                my_json = json.load(my_File)
                print("DATE", "\t\t", "LOCAL TEAM", "\t\t", "VISITOR TEAM", "\t\t", "LOCAL WINER", "\t\t", 
                        "VISITOR WINER", "\t\t", "DRAW")
                print("============================================================\
=========================================================")
                for my_data in my_json["data"]:
                    
                    if len(my_data["local_team"]) < 6 and len(my_data["visitor_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["local_team"]) < 6 and len(my_data["visitor_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", my_data["visitor_team"], 
                                "\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["local_team"]) >= 14 and len(my_data["visitor_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["local_team"]) >= 14 and len(my_data["visitor_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])

                    elif len(my_data["local_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", my_data["visitor_team"], 
                                "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["visitor_team"]) < 6:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])

                    elif len(my_data["local_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t", my_data["visitor_team"], 
                                "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    elif len(my_data["visitor_team"]) >= 14:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])
                    else:
                        print(my_data["date"], "\t", my_data["local_team"], "\t\t", my_data["visitor_team"], 
                                "\t\t", my_data["local_winer"], "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])


    def solo_command(self, command_line):
        if command_line.lower() == 'clean':
            system("cls")
        elif command_line.lower() == 'listcommand' or command_line.lower() == 'help':
            for command, utility in self.command_list.items():
                if len(command) <= 6:
                    print(command.upper(),"\t\t",utility)
                else:
                    print(command.upper(),"\t",utility)
        elif command_line.lower() in self.detail_command.keys():
            print(f"The command '{command_line}' need more parameters. Type it with 'help' to more information")
        else:
            print(f"'{command_line}' isn't a inner command of this program")

    def failure(self, match_R):
        result_list = {
            float(match_R["local_winer"]),
            float(match_R["visitor_winer"]),
            float(match_R["draw"])
            }
        my_value = []
        my_value.insert(0, result_list.pop(result_list.index(min(result_list))))
        my_value.insert(0, result_list.pop(result_list.index(min(result_list))))
        while True:
            result_match = input(f'1._local \n2._visitor \n3._draw\
                    \nselect the resul between {match_R["local_team"]} & {match_R["visitor_team"]}: ')
            if failure == 'y':
                


    def resultbets_command(self):
        directory1 = "./BETS_DATAS/bets_Results.json"
        directory2 = "./BETS_DATAS/recomended_Bets.json"

        recomended_Bets_file = open(directory2)
        my_data = json.load(recomended_Bets_file)
        recomended_Bets_file.close()

        for match_bet in my_data["data"]:
            result_match = input(f'type the resul between {match_bet["local_team"]} & {match_bet["visitor_team"]}: ')

            my_dict = {
                'league': match_bet["league"],
                'date': match_bet["date"],
                'local_team': match_bet["local_team"],
                'visitor_team': match_bet["visitor_team"],
                'local_winer': match_bet["local_winer"],
                'visitor_winer': match_bet["visitor_winer"],
                'draw': match_bet["draw"],
                'result': 
            }






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
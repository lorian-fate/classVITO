from itertools import combinations
import random



def create_pairings(participants_list):
    return [participants for participants in combinations(participants_list, 2)]


def create_rounds(pairings_list, participants_quantity):
    rounds_list = []
    single_round_list = []
    checker_list = []
    round_quantity = participants_quantity / 2
    counter = 0
    backup_counter = 0

    while len(pairings_list) != 0:
        

        for match_tournament in pairings_list:
            if len(checker_list) == 0:
                checker_list.append(match_tournament[0])
                checker_list.append(match_tournament[1])
                single_round_list.insert(0, pairings_list.pop(pairings_list.index(match_tournament)))
            
            else:
                if match_tournament[0] not in checker_list and match_tournament[1] not in checker_list:
                    checker_list.append(match_tournament[0])
                    checker_list.append(match_tournament[1])
                    single_round_list.insert(0, pairings_list.pop(pairings_list.index(match_tournament)))

                elif len(single_round_list) == round_quantity:
                    rounds_list.append(single_round_list)
                    single_round_list = []
                    checker_list = []
                    counter = 0
                    backup_counter = 0
        counter += 1
        backup_counter += 1
        if counter == 5:
            for match_tournament in single_round_list:
                pairings_list.insert(0, single_round_list.pop(single_round_list.index(match_tournament)))
            if len(single_round_list) != 0:
                for match_tournament in single_round_list:
                    pairings_list.insert(0, single_round_list.pop(single_round_list.index(match_tournament)))
            
            random.shuffle(pairings_list)
            checker_list = []
            counter = 0
            #random_match = random.choice(pairings_list)
            #checker_list.append(random_match[0])
            #checker_list.append(random_match[1])
            #single_round_list.insert(0, pairings_list.pop(pairings_list.index(random_match)))

        if backup_counter == 10:
            for match_tournament_b in rounds_list:
                for match_tournament in match_tournament_b:
                    pairings_list.insert(0, rounds_list.pop(rounds_list.index(match_tournament)))

                    
            if len(rounds_list) != 0:
                for match_tournament_b in rounds_list:
                    for match_tournament in match_tournament_b:
                        pairings_list.insert(0, rounds_list.pop(rounds_list.index(match_tournament)))


            #random.shuffle(pairings_list)
            checker_list = []
            single_round_list = []
            backup_counter = 0

            

    if len(single_round_list) != 0:
        rounds_list.append(single_round_list)
    return rounds_list

                
def show_rounds():
    participants = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    match_list = create_pairings(participants)
    rounds_list = create_rounds(match_list, len(participants))

    print("=========================================================================")
    for numerator, rounds in enumerate(rounds_list, start=1):
        print(f"\nROUND {numerator}: ")
        print("\n|--------------------------------------------------------------------------------------|")
        for round_t in rounds:
            print(f"\t{round_t[0]} v {round_t[1]}\t", end='|')
        print("\n|--------------------------------------------------------------------------------------|")

    return ''


show_rounds() 


import math

"""
    #! al prescindir del valor más alto te arriegas a perder la apuesta
    #! si el resultado del partido corresponde al valor del valor prescindido,
    #! No obstante esta perdida se puede recuperar si solo se pierden dos o 
    #! menos apuestas no más
"""

def my_BETS():
    value1 = 4.20
    value2 = 1.61
    porcetage_value1 = (value2*100)/(value2 + value1)
    porcetage_value2 = (value1*100)/(value1 + value2)
    stock = 200
    stock_to_bet = 20
    heap_to_bet_value1 = (stock_to_bet/100)*porcetage_value1
    heap_to_bet_value2 = (stock_to_bet/100)*porcetage_value2

    print(heap_to_bet_value1, heap_to_bet_value2)    
    if heap_to_bet_value1 > heap_to_bet_value2:
        new_heap_to_bet_value1 = str(heap_to_bet_value1).split(".")
        my_list = ["0", str(new_heap_to_bet_value1[1])]
        decimal = float('.'.join(my_list))
        heap_to_bet_value2 = decimal + heap_to_bet_value2
        return f"To the value {value1} you must to bet {int(new_heap_to_bet_value1[0])}\
                \nTo the value {value2} you must to bet {int(heap_to_bet_value2)}"

    elif heap_to_bet_value2 > heap_to_bet_value1:
        new_heap_to_bet_value2 = str(heap_to_bet_value2).split(".")
        my_list = ["0", str(new_heap_to_bet_value2[1])]
        decimal = float('.'.join(my_list))
        heap_to_bet_value1 = decimal + heap_to_bet_value1
        return f"To the value {value1} you must to bet {int(heap_to_bet_value1)} \
                \nTo the value {value2} you must to bet {int(new_heap_to_bet_value2[0])}"

print(my_BETS())




















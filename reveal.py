from random import randint, choice
# from total_count import estimate


from check_bets import bettings
list_list_numbers = range(1, 31)



def count(total):
    win = randint(1, 31)
    # print(win)
    bet_number, bet_money = bettings(list_numbers=list_list_numbers, total=total)
    reveal_money = 0
    lost_money = 0

    if bet_number == win:
        reveal_money += bet_money * 2
        print('Great! you won this round', reveal_money)

    else:
        lost_money += bet_money
        print('Sorry! You lost this round', lost_money)


    return reveal_money, lost_money






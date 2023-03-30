# from total_count import estimate
#
# total, lost_in_all = estimate()
# from reveal import
from bet_checking import doublecheck_number, doublecheck_money


def bettings(list_numbers, total):
    try:
        print(f'list of numbers {list_numbers}')
        bet_number = int(input(f' bet number: '))
        if bet_number not in list_numbers:
            bet_number = doublecheck_number(bet_number, list_numbers)
    except:
        while True:
            try:
                print('It must be number(in list)')
                bet_number = int(input(' Try again: '))
                if type(bet_number) == int and bet_number in list_numbers:
                    break
            except:
                True

    if total > 0:
        # print(total)
        try:
            bet_money = int(input(' How much money do you bet:  '))

            if total > 0 and total < bet_money:
                bet_money = doublecheck_money(total)
        except:
            while True:
                try:
                    print(f'You have only {total}')
                    bet_money = int(input(' Try again: '))
                    if total > 0 and total >= bet_money:
                        break
                except:
                    True

    return bet_number, bet_money

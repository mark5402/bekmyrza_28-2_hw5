def doublecheck_number(bet, list_numbers):
    # print('double check')
    if bet not in list_numbers:
        while True:
            try:
                print('It must be number(in list)')
                bet = int(input(' Try again: '))
                if type(bet) == int and bet in list_numbers:
                    return bet
            except:
                True

def doublecheck_money(total):
    while True:
        try:
            print(f'You have only {total}')
            bet_money = int(input(' Try again: '))
            if total > 0 and total >= bet_money:
                return bet_money
        except:
            True
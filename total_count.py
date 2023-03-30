from reveal import count
from decouple import config


def estimate(total):
    # total = config('MY_MONEY')
    # total = int(total)
    game_going = True
    lost_in_all = 0
    while game_going:
        print('start')
        # print(f'total {total}')
        reveal_money, lost_money = count(total)
        lost_in_all += lost_money
        total += reveal_money
        total -= lost_in_all

        stop_game = input(' Do you want to play on(y/n):')
        if stop_game != 'y' or total <= 0:
            print(f'On yor accaoun {total}')
            return total, lost_in_all, reveal_money

        else:
            game_going = True

        # return total, lost_in_all, reveal_money
        # stop_game = input(' (y/n):')

    # return total, lost_in_all

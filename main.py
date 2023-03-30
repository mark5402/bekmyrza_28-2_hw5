# #ДЗУрок5 Дэдлайн 23.03.2023 23 59
# ДЗ*:
# 1. Установить в свою виртуальную среду проекта внешний модуль python-decouple
# 2. В файле requirements.txt зафиксировать зависимости проекта с помощью команды pip freeze
# 3. Создать многомодульную игру Казино
# 4. Сам запуск игры в отдельном файле
# 5. Логика выигрыша или проигрыша в отдельном файле
# Правила игры такие :
# A. Есть массив из чисел от 1 до 30, каждый раз вы делаете ставку на определенную слоту из чисел и ставите деньги
# B. Рандомно выбирается выигрышная слота, если вы выигрываете,
# вам причисляется удвоенная сумма, той которую вы поставили,
# если вы загадали невыигрышную слоту - теряете поставленную сумму
# C. В начале игры у вас также есть деньги например 1000$, но в конце мы понимаем вы в выигрыше или в проигрыше
# D. значение переменной начального капитала должно считываться с системной переменной под названием MY_MONEY из файла settings.ini
# E. После каждой ставки вам задается вопрос хотите ли вы сыграть еще, если да - то делаете ставку, если нет - то подводится итог игры

from random import randint, choice
from decouple import config

from reveal import count
from total_count import estimate
# from win import did_you_win


def game():
    total = config('MY_MONEY')
    total = int(total)
    # print(total)
    # game_going = True
    # lost_in_all = 0
    # while game_going:
    # print('start')
    # stop_game, reveal_money, lost_money = estimate()
    # lost_in_all += lost_money
    # total += reveal_money - lost_money
    #
    # reveal_money, lost_money = count()
    # total += reveal_money - lost_money
    # print(reveal_money)
    # print('total 1', total)

    # estimate()
        # print(total)
        # if stop_game != 'y':
        #     print('yy')
        #     print('total 2', total)
        #     did_you_win()
        #     return total, lost_in_all

        #
        # else:
        #     game_going = True\
        # total -= losts

    total, losts, reveal = estimate(total)
    if total > int(config('MY_MONEY')):
        print(f'you won {reveal} and lost {losts} at all\n'
              f'on you accaount {total}\n'
              f' you played good today')
    else:
        print(f'you won {reveal} and lost {losts} at all\n'
              f'on you accaount {total}\n'
              f'It ok, nex time')






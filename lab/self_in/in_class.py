# def read_fruits(fruit_basket):
#     _list = []
#     word = input('Enter choice or quit: ')
#     while word != 'quit':
#         if word in fruit_basket:
#             _list.append(word)
#         else:
#             print('Your fruit choice is not available.')
#         word = input('Enter choice or quit: ')
#     return _list
#
#
# def print_price(fruit_price, choice_list):
#     """
#     For price printing
#     :param fruit_price:
#     :param choice_list:
#     :return:
#     >>> print_price(fruit_price, ['apple', 'banana', 'melon'])
#     apple : 20 Baht
#     banana : 10 Baht
#     melon : 15 Baht
#     """
#     for i in choice_list:
#         print(f'{i} : {fruit_price.get(i)} Baht')
#
#
# def compute_total_price(fruit_price, choice_list):
#     """
#     For summarize the total prize
#     :param fruit_price:
#     :param choice_list:
#     :return:
#     >>> compute_total_price(fruit_price, ['apple', 'banana', 'melon'])
#     45
#     >>> compute_total_price(fruit_price, ['apple', 'banana', 'melon', 'melon'])
#     60
#     """
#     out = sum(fruit_price.get(i) for i in choice_list)
#     return out
#
#
# fruit_basket = ['apple', 'banana', 'orange', 'melon']
# fruit_price = {'apple': 20, 'banana': 10, 'orange': 5, 'melon': 15}
#
# basket = read_fruits(fruit_basket)
# print(basket)
# print_price(fruit_price, basket)
# total_price = compute_total_price(fruit_price, basket)
# print(f'Total price = {total_price:.2f} Baht')


# def read_fruits(fruit_basket):
#     _dic = {}
#     word = input('Enter choice or quit: ')
#     while word != 'quit':
#         if word in fruit_basket:
#             name = input('Enter name: ')
#             _dic[name] = word
#         else:
#             print('Your fruit choice is not available.')
#         word = input('Enter choice or quit: ')
#     return _dic
#
#
# def print_price(fruit_price, choice_dict):
#     for i in choice_dict:
#         print(f'{i} pays {fruit_price.get(choice_dict[i]):.2f} Baht')


# basket = read_fruits(fruit_basket)
# print(basket)
# name_out = input('Enter name to removed: ')
# if basket != {}:
#     basket.pop(name_out)
#     print(f'After remove\n{basket}')
# else:
#     print('Dictionary is empty. Cannot perform removal.')

def q11():
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    i, j = 0, 0
    while i < n:
        j = 0
        while j < m:
            print(f'{i},{j}')
            j += 1
        i += 1


def q12():
    x = int(input('Enter start for outer loop: '))
    y = int(input('Enter start for inner loop: '))
    z = int(input('Enter stop for outer loop: '))
    w = int(input('Enter stop for inner loop: '))
    a = int(input('Enter step for outer loop: '))
    b = int(input('Enter step for inner loop: '))

    i, j = x, y
    while i < z:
        j = y
        while j > w:
            print(f'{i},{j}')
            j += b
        i += a


def q21():
    x = int(input('Enter x: '))
    _sum, count = 0, 0
    while x != -99:
        _sum += x
        count += 1
        x = int(input('Enter x: '))
    print(f'Sum of {count} x\'s = {_sum}')


def q22():
    _all_sum, _all_count = 0, 0
    _sum = 0
    word = ''
    while word != 'q':
        _sum = 0
        count = 0
        x = int(input('Enter x: '))
        while x != -99:
            _sum += x
            x = int(input('Enter x: '))
            count += 1
        _all_sum += _sum
        _all_count += count
        print(f'Sum of {count} x\'s = {_sum}')
        print(f'Cumulative sum of {_all_count} x\'s = {_all_sum}')
        word = input('Continue or quit (q for quit): ')
        print()


def q23():
    def read_count_and_sum_x():
        _sum, count = 0, 0
        x = int(input('Enter x: '))
        while x != -99:
            _sum += x
            x = int(input('Enter x: '))
            count += 1
        return _sum, count

    q = ''
    _round = 1
    total_sum, total_counts = 0, 0
    while q != 'q':
        print(f'Round {_round}:')
        _sums, counts = read_count_and_sum_x()
        total_sum += _sums
        total_counts += counts
        print(f'Sum of {counts} x\'s = {_sums}')
        print(f'Cumulative sum of {total_counts} x\'s = {total_sum}')
        q = input('Continue or quit (q for quit): ')
        print()
        _round += 1


def q24():
    def read_cumulative_count_and_sum_x(cum_sum, cum_count):
        _sum, count = cum_sum, cum_count
        x = int(input('Enter x: '))
        while x != -99:
            _sum += x
            x = int(input('Enter x: '))
            count += 1
        return _sum, count

    q = ''
    _round = 1
    t_sum, t_counts = 0, 0
    while q != 'q':
        t_sum, t_counts = read_cumulative_count_and_sum_x(t_sum, t_counts)
        print(f'Round {_round}: Cumulative sum of {t_counts} x\'s = {t_sum}')
        q = input('Continue or quit (q for quit): ')
        print()
        _round += 1


def q25():
    def read_list_x():
        _sum = []
        x = int(input('Enter x: '))
        while x != -99:
            _sum.append(x)
            x = int(input('Enter x: '))
        return _sum

    _quit = ''
    _round = 1
    all_list, total_counts = [], 0
    _sum = 0
    while _quit != 'q':
        print(f'Round {_round}:')
        _list = read_list_x()
        all_list.append(_list)
        total_counts += len(_list)
        _sum += sum(_list)
        print(f'Current list of x\'s = {_list}')
        print(f'Current nested list of x\'s = {all_list}')
        print(f'Cumulative sum of {total_counts} x\'s = {_sum}')
        _quit = input('Continue or quit (q for quit): ')
        print()
        _round += 1


def q41():
    def factorial(x):
        fac = 1
        for i in range(1, x + 1):
            fac *= i
        return fac

    k = int(input('Input k: '))
    _sum = 0
    for _round in range(1, k + 1):
        print(f'{_round}! = {factorial(_round)}')
        _sum += factorial(_round)
    print(f'Summation of factorial {1}!-{k}! = {_sum}')

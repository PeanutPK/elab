# num = int(input('Input k: '))
# i, _fac, _sum = 1, 1, 0
# while i <= num:
#     _fac *= i
#     print(f'{i}! = {_fac}')
#     _sum += _fac
#     i += 1
# print(f'Summation of factorial 1!-{num}! = {_sum}')


def list_factors(n):
    """
   Get string of factors of n
   :params n is an integer to find factors
   :return string of factors (with a comma and a 1-space between each factor)
   >>> list_factors(6)
   '1, 2, 3, 6, '
   >>> list_factors(7)
   '1, 7, '
   >>> list_factors(12)
   '1, 2, 3, 4, 6, 12, '
   """
    _str = ''
    for i in range(1, n + 1):
        if n % i == 0:
            _str += str(i) + ', '
    return _str


def find_sum_and_num_factors(n):
    """
    Find summation and count number of factors of n
    :params n is an integer to find factors
    :return sum is summation of factors of n
            count is number of factors of n
    >>> find_sum_and_num_factors(6)
    (12, 4)
    >>> find_sum_and_num_factors(7)
    (8, 2)
    >>> find_sum_and_num_factors(12)
    (28, 6)
    """
    _sum = []
    for i in range(1, n + 1):
        if n % i == 0:
            _sum += [int(i)]
    return sum(_sum), len(_sum)


# ============================================================================
# Q 4.1
# n = int(input('Enter positive number: '))
# _list = list_factors(n)
# _sum_f, _num_f = find_sum_and_num_factors(n)
# print(f'Factors of {n} are {_list}\n'
#       f'Number of factors is {_num_f}\n'
#       f'Sum of {_list} is {_sum_f}')
# if _num_f != 2:
#     print(f'{n} is not prime number')
# elif _num_f == 2:
#     print(f'{n} is prime number')
# else:
#     print('Program ends.')
# ============================================================================

# ============================================================================
# Q 4.2
# N = int(input('Please input N : '))
# prime, count = 0, 0
# while True:
#     if N < 0:
#         print(f'Program reads {count} numbers. {prime} of them are prime.')
#         print('Program ends.')
#         break
#     _list = list_factors(N)
#     _sum_f, _num_f = find_sum_and_num_factors(N)
#     print(f'Factors of {N} are {_list}\n'
#           f'Number of factors is {_num_f}\n'
#           f'Sum of {_list} is {_sum_f}')
#     if _num_f != 2:
#         print(f'{N} is not prime number')
#     else:
#         print(f'{N} is prime number')
#         prime += 1
#     print()
#     count += 1
#     N = int(input('Please input N : '))
# ============================================================================


# Q 5.1
# def count_digits(number):
#     pass
#

def get_last_digit(n):
    """
    Get last digit in number
    :params number is an integer
    :return last digit in number

    >>> get_last_digit(41)
    1
    >>> get_last_digit(394)
    4
    >>> get_last_digit(1020)
    0
    """
    for i in range(len(str(n))):
        n %= 10**(i+1)
    return n


def get_distribution(number):
    """
    Return string showing distribution of number
    :params number (int): a number to find distribution
    :return string
    >>> get_distribution(21)
    '1x10^0 + 2x10^1'
    >>> get_distribution(306)
    '6x10^0 + 0x10^1 + 3x10^2'
    >>> get_distribution(12201)
    '1x10^0 + 0x10^1 + 2x10^2 + 2x10^3 + 1x10^4'
    """
    _str = ''
    snum = str(number)
    for i in range(len(snum) - 1):
        _str += snum[len(snum) - 1 - i] + 'x10^' + str(i) + ' + '
    _str += snum[0] + 'x10^' + str(len(snum) - 1)
    return _str


# num = int(input('Input number: '))


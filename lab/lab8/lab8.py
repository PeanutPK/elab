# for i in range(5, 10):
#     print(f"i = {i}")
#     for j in range(1, 3):
#         print(f"  j = {j}")


# def f(n):
#     sum = 0
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             sum = sum + j + i
#     return sum


# for i in range(1,6):
#     print(f"i = {i}")
#     for j in range(i,0,-1):
#         print(f"  j = {j}")


# num = int(input('Enter number of levels: '))
# size = int(input('Enter size of each bush: '))
# for i in range(num):
#     for j in range(size):
#         nspaces = size-j-1
#         nstars = 2*j+1
#         print((' ' * nspaces) + ('*' * nstars))


# def f(n):
#     """
#     Compute value of function f
#     :params n: is the number to compute value of function f
#     :return: value of function f
#     >>> f(1)
#     1.0
#     >>> f(2)
#     1.5
#     >>> f(3)
#     1.8333333333333333
#     >>> f(10)
#     2.9289682539682538
#     """
#     out = 0
#     for i in range(1, n + 1):
#         out += 1 / i
#     return out
#
#
# n = int(input("Input n: "))
# print(" n | f(n)")
# print("---+------")
# for i in range(1, n+1):
#     print(f'{i:^3}| {f(i):.3f}')


def isPrime(number):
    """
    Check if the number is prime number
    :params number: is the number to check if is prime number
    :return: True if the number is prime number
             False if the number isn't prime number
    >>> isPrime(1)
    False
    >>> isPrime(2)
    True
    >>> isPrime(3)
    True
    >>> isPrime(1231)
    True
    >>> isPrime(14)
    False
    """
    if number != 1 and number != 0:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return False


def printAllPrimes(limit):
    """
    Print all the prime number between 1 to the limit
    >>> printAllPrimes(10)
    2 3 5 7
    >>> printAllPrimes(20)
    2 3 5 7 11 13 17 19
    >>> printAllPrimes(0)

    >>> printAllPrimes(2)
    2
    >>> printAllPrimes(3)
    2 3
    """
    s = []
    if 1 < limit < 1000:
        for i in range(limit + 1):
            if isPrime(i) is True:
                s.append(i)
        print(*s, sep=' ')


number = int(input("Input n: "))
printAllPrimes(number)

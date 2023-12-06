# def add(a, b):
#     ans = a + b
#     return ans
#
#
# def subtract(a, b):
#     ans = a - b
#     return ans
#
#
# def multiply(a, b):
#     ans = a * b
#     return ans
#
#
# def divide(a, b):
#     ans = a / b
#     return ans
#
#
# def int_divide(a, b):
#     ans1 = a // b
#     ans2 = a % b
#     return ans1, ans2
#
#
# def display_result(a, b, op, result):
#     print(f'{a:.2f} {op} {b:.2f} = {result:.2f}')
#
#
# def calculate_and_display(a, b, op):
#     ans = ans2 = 0
#     if op == '+':
#         ans = add(a, b)
#     elif op == '-':
#         ans = subtract(a, b)
#     elif op == '*':
#         ans = multiply(a, b)
#     elif op == '/':
#         ans = divide(a, b)
#     elif op == '//':
#         ans, ans2 = int_divide(a, b)
#     else:
#         pass
#     display_result(a, b, op, ans)
#     if op == '//':
#         display_result(a, b, '%', ans2)
#
#
# x = float(input('Enter first number: '))
# y = float(input('Enter second number: '))
# op = input('Enter operation: ')
# calculate_and_display(x, y, op)


# def read_one_int(message):
#     number = int(input(message))
#     return number
#
#
# n = read_one_int('Enter n: ')
# for i in range(1, int(n) + 1):
#     a = float(input(f'Enter value{i}: '))
#     print(f'You enter {a:.1f}')


# def read_one_int(message):
#     number = int(input(message))
#     return number
#
#
# n = read_one_int('Enter n: ')
# s = 0
# for i in range(1, int(n) + 1):
#     a = float(input(f'Enter value{i}: '))
#     s += a
#     print(f'So far, sum of entered values = {s:.2f}')
#
# print(f'Final sum = {s:.2f}')


# def read_one_int(message):
#     number = int(input(message))
#     return number
#
#
# n = read_one_int('Enter n: ')
# s = []
# for i in range(1, int(n) + 1):
#     a = float(input(f'Enter value{i}: '))
#     s.append(a)
#     print(s)
# print('Final list is:')
# print(s)


# def read_one_int(message):
#     number = int(input(message))
#     return number
#
#
# n = read_one_int('Enter n: ')
# l, s = [], 0
# for i in range(1, int(n) + 1):
#     a = float(input(f'Enter value{i}: '))
#     l.append(a)
#     s += a
# print('Final list is:')
# print(l)
# print(f'Sum of values = {s:.2f}')
# print(f'Minimum value = {min(l):.2f}\n'
#       f'Maximum value = {max(l):.2f}')
# print('Values of list are:')
# for i in l:
#     print(f'{i:.3f}')


# def read_one_int(message):
#     number = int(input(message))
#     return number
#
#
# n = read_one_int('Enter n: ')
# l = []
# for i in range(1, int(n) + 1):
#     a = float(input(f'Enter value{i}: '))
#     l.append(a)
# print('Final list is:')
# print(l)
# x = float(input('Enter x: '))
# for i in range(len(l)):
#     l[i] += x
# print('Result list is:')
# print(l)


# def read_one_int(message):
#     number = int(input(message))
#     return number
#
#
# n = read_one_int('Enter n: ')
# l = []
# for i in range(1, n + 1):
#     a = float(input(f'Enter value{i}: '))
#     l.append(a)
# print('Final list is:')
# print(l)
# m = read_one_int('Enter m: ')
# for i in range(1, m + 1):
#     print(f'Round {i}')
#     index = read_one_int('Enter index: ')
#     x = float(input('Enter x: '))
#     l[index] += x
#     print('Current list is:')
#     print(l)
# print('Result list is:')
# print(l)


# msg = input("What do you want me to say? ")
# num = int(input("How many times you want me to say it? "))
#
# for i in range(1,num+1):
#     print(f'{msg} #{i}')

# s = input()
# a=''
# for i in range(len(s)):
#     if s[i].isupper():
#         a+=str(i)
# print(','.join(a))

# seq = [2, 3, 5, 7, 11, 13, 17, 19]
# for i in range(len(seq)-1,-1,-1):
#     print(seq[i])

# _set = []
# while True:
#     s = input('Enter student score (or ENTER to finish): ')
#     if s == '':
#         break
#     _set.append(int(s))
# for i in range(len(_set)):
#     print(f'Score #{i + 1}: {_set[i]}')
#
# avg = sum(_set)/len(_set)
# _max = max(_set)
# _min = min(_set)
# print(f'Average score is {avg:.2f}')
# print(f'Minimum score is {_min}')
# print(f'Maximum score is {_max}')


# _set = []
# n = int(input('How many students? '))
# for i in range(n):
#     s = input('Enter student score: ')
#     _set.append(int(s))
# for i in range(len(_set)):
#     print(f'Score #{i + 1}: {_set[i]}')
#
# avg = sum(_set)/len(_set)
# _max = max(_set)
# _min = min(_set)
# print(f'Average score is {avg:.2f}')
# print(f'Minimum score is {_min}')
# print(f'Maximum score is {_max}')


# s = input('Enter a message: ')
# a = s.count('a')
# e = s.count('e')
# i = s.count('i')
# o = s.count('o')
# u = s.count('u')
# print(f'There are {a} a\'s.')
# print(f'There are {e} e\'s.')
# print(f'There are {i} i\'s.')
# print(f'There are {o} o\'s.')
# print(f'There are {u} u\'s.')
# print(f'There are {len(s)-a-e-i-o-u} non-vowels characters.')


# w = input('Enter word: ')
# s = w.lower()
# if s == s[::-1]:
#     print(f'{w} is palindrome')
# else:
#     print(f'{w} is not palindrome')


s = input('Enter a decoded message: ')
if 'ya' in s[:-3:-1]:
    s = s[-3::-1]
print('The decoded message is:')
print(s.replace('z', 's')
      .replace('e', 'a')
      .replace('o', 'e'))

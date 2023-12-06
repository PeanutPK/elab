# def f(x):
#     if x <= 15:
#         answer = 2 * x + 10
#     elif x <= 35:
#         answer = 3 * x * x
#     else:
#         answer = 2 * x ** 3 - 5
#     print(f'f({x:.3f}) = {answer:.3f}')
#
#
# rn = float(input('Enter a real number: '))
# f(rn)


# print('Input a point (x,y):')
# x = float(input('x = ? '))
# y = float(input('y = ? '))
# if x > 0 and y > 0:
#     print(f'The point ({x:.2f},{y:.2f}) is in quadrant 1.')
# elif x < 0 < y:
#     print(f'The point ({x:.2f},{y:.2f}) is in quadrant 2.')
# elif x < 0 and y < 0:
#     print(f'The point ({x:.2f},{y:.2f}) is in quadrant 3.')
# elif x > 0 > y:
#     print(f'The point ({x:.2f},{y:.2f}) is in quadrant 4.')
# elif x == 0 and y != 0:
#     print(f'The point ({x:.2f},{y:.2f}) is on the y-axis.')
# elif x != 0 and y == 0:
#     print(f'The point ({x:.2f},{y:.2f}) is on the x-axis.')
# elif x == 0 and y == 0:
#     print(f'The point ({x:.2f},{y:.2f}) is at the origin.')


a = float(input('Enter 1st line\'s length: '))
b = float(input('Enter 2nd line\'s length: '))
c = float(input('Enter 3rd line\'s length: '))

l1 = max(a, b, c)
l2 = min(a, b, c)
l3 = a + b + c - l1 - l2

l12 = l1 ** 2
l22 = l2 ** 2
l32 = l3 ** 2

if l1 > 0 and l2 > 0 and l3 > 0:
    if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
        if l12 != (l22 + l32) and l22 != (l12 + l32) and l32 != (l22 + l12):
            print('It\'s a triangle but not a right triangle.')
        elif l1 % 1.5 == 0 and l2 % 2.5 == 0 and l3 % 2 == 0 and l32 == l22 + l12:
            print('It\'s a right triangle.')
        else:
            print('It\'s a right triangle.')
    else:
        print('It\'s not a triangle.')
else:
    print('It\'s not a triangle.')

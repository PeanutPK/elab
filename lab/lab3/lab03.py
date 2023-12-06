def rectangle_area(length, width):
    area = length * width
    return area


def compute_double(value):
    return value * 2


def print_double(value):
    print(value * 2)


def compute_circle_area(r):
    area = pi * (r ** 2)
    return area


def compute_circle_circumference(r):
    circumference = 2 * pi * r
    return circumference


def round_to_full_hour(minutes):
    hours = ceil(minutes / 60)
    return hours


def get_parking_payment(hours, rate):
    payment = hours * rate
    return payment


def compute_sphere_volume(radius):
    volume = (4 / 3) * pi * (radius ** 3)
    return volume


def compute_sphere_surface_area(radius):
    area = 4 * pi * (radius ** 2)
    return area


def compute_total_savings(principal, interest_rate, number_of_years):
    total_money = principal * ((1 + (interest_rate / 100)) ** number_of_years)
    return total_money


def add(first, second):
    out = first + second
    return out


def subtract(first, second):
    out = first - second
    return out


def multiply(first, second):
    out = first * second
    return out


def divide(first, second):
    out = first / second
    return out


def calculate(first, second, operand):
    result = 0
    if operand == '+':
        result = add(first, second)
    elif operand == '-':
        result = subtract(first, second)
    elif operand == '*':
        result = multiply(first, second)
    elif operand == '/':
        result = divide(first, second)
    return result


def change_log_base(x, a, b):
    out = log(x, b) / log(a, b)
    return out


def compute_rectangle_area(first_side, second_side):
    area = first_side * second_side
    return area


def compute_surface_area(width, length, height):
    surface_area = compute_rectangle_area(width, length) * 2 + compute_rectangle_area(width, height) * 2 + compute_rectangle_area(height, length) * 2
    return surface_area


def compute_volume(width,length,height):
    volume = width * length * height
    return volume


from math import pi, ceil, log

for _ in range(4):
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))
    area = compute_rectangle_area(width, length)
    print(f"Rectangle area = {area:.3f}")

# w = float(input('Enter width: '))
# l = float(input('Enter length: '))
# h = float(input('Enter height: '))
# print(f'For [{w:.2f} x {l:.2f} x {h:.2f}] cuboid:')
# print(f'Surface area = {compute_surface_area(w, l, h):.3f}')
# print(f'Volume = {compute_volume(w,l,h):.3f}')
# print()
# print('After doubling each side,')
# print(f'For [{2*w:.2f} x {2*l:.2f} x {2*h:.2f}] cuboid:')
# print(f'Surface area = {compute_surface_area(2*w, 2*l, 2*h):.3f}')
# print(f'Volume = {compute_volume(2*w,2*l,2*h):.3f}')

# x = float(input('Enter value of x: '))
# a = float(input('Enter value of a: '))
# b = float(input('Enter value of b: '))
# print(f'Logarithm of {x:.3f} with base {a:.3f} = {log(x, a):.3f}')
# print(f'Logarithm of {x:.3f} with base {b:.3f} / Logarithm of {a:.3f} with base {b:.3f} = {change_log_base(x, a, b):.3f}')

# fs = float(input('Enter value of the first number: '))
# sn = float(input('Enter value of the second number: '))
# op = input('Enter value of the operator: ')
# print(f'{fs:.2f} {op} {sn:.2f} = {calculate(fs, sn, op):.2f}')

# p = float(input('Please enter principal: '))
# ir = float(input('Please enter interest rate: '))
# y = int(input('Please enter number of years: '))
# print(f'Total savings amount after {y} years is {compute_total_savings(p,ir,y):.2f} Baht.')

# r = float(input('What is the radius of the sphere? '))
# print(f'The volume of the sphere is {compute_sphere_volume(r):.2f}.')
# print(f'The surface area of the sphere is {compute_sphere_surface_area(r):.2f}.')

# time_minute = int(input('Enter parking duration in minutes: '))
# hour = round_to_full_hour(time_minute)
# print('The parking fee rate is 30 Baht per hour.')
# print(f'You will pay {get_parking_payment(hour,30)} Baht for parking {time_minute} minutes.')

# w = float(input('Enter the value of width: '))
# l = float(input('Enter the value of length: '))
# r = float(input('Enter the value of diameter: ')) / 2
# print(f'The area of the lawn is {compute_rectangle_area(w, l)-compute_circle_area(r):.2f} sq.m.')
# print(f'The area of the circle is {compute_circle_area(r):.2f}.')
# print(f'The circumference of the circle is {compute_circle_circumference(r):.2f}.')

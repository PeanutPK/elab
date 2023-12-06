# def usd_to_thb(usd):
#     global EXCHANGE_RATE
#     return usd*EXCHANGE_RATE
#
# EXCHANGE_RATE = 34.09
# print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
# print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")
#
# EXCHANGE_RATE = 33.15
# print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
# print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")
#
# EXCHANGE_RATE = 35.26
# print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
# print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")


# def read_triangle_inputs():
#     base = float(input("Enter triangle base: "))
#     height = float(input("Enter triangle height: "))
#     return base, height
#
#
# def compute_triangle_area(base, height):
#     a = 0.5 * base * height
#     return a
#
#
# base, height = read_triangle_inputs()
# area = compute_triangle_area(base, height)
# print(f"Triangle\'s area = {area:.3f}")


# first, last = 'Sam', 'Smith'
# date, month, year = 16, 5, 2002
# print(f'My name is {first}',end=' ')
# print(f'{last}',end='\n')
# print(f'My birthday',end=' : ')
# print(date, month, year,sep='/')
# print(f'In 2023, I a',end='')
# print(f'm {2023 - year} years old.',end='')


# first, last = 'Sam', 'Smith'
# date, month, year = 16, 5, 2002
# height = 176.54273
# print('My name is {} {}'.format(first, last))
# print('I was born on {}/{}/{}'.format(date, month, year))
# print('I am {:.3f} cm. tall.'.format(height))
#
# table_num, num_guests = 7, 5
# reserved_time = "11:00-13:00"
# n_desserts, n_app, n_entrees = 2, 3, 5
# cost = 4318.1685
# print('Table #{} is reserved at {} for {} people.'.format(table_num, reserved_time, num_guests))
# print('Customers pre-orders {} appetizers, {} entrees, and {} desserts.'.format(n_app, n_entrees, n_desserts))
# print('After discount, the bill costs {:.2f} Baht.'.format(cost))


# def read_weight_height():
#     weight = float(input('What is your weight (kg)? '))
#     height = float(input('What is your height (cm)? '))
#     return weight, height
#
#
# def get_bmi(weight,height):
#     bmi = weight/((height/100)**2)
#     return bmi
#
#
# weight, height = read_weight_height()
# bmi = get_bmi(height=height, weight=weight)
# print(f'Your Body Mass Index (BMI) is {bmi:.2f}')


# def read_trapezoid():
#     print('Please specify your trapezoid\'s properties.')
#     a = float(input('What is the length of side a: '))
#     b = float(input('What is the length of side b: '))
#     h = float(input('What is the height? '))
#     return a, b, h
#
#
# def trapezoid_area(a, b, h):
#     area = ((a + b) / 2) * h
#     return area
#
#
# side1, side2, height = read_trapezoid()
# area = trapezoid_area(b=side2, h=height, a=side1)
# print(f'Trapezoid\'s area is {area:.2f}')


# KILOMETERS_PER_MILE = 1.609
#
#
# def convert_miles_to_kms(miles):
#     kilometers = miles * KILOMETERS_PER_MILE
#     return kilometers
#
#
# miles = float(input('What is your distance in miles? '))
# kilometers = convert_miles_to_kms(miles)
# print(f'After conversion, the distance is {kilometers:.2f} kilometers.')


# FIVEHUNDRED = 500
# HUNDRED = 100
# TWENTY = 20
#
#
# def read_all_inputs():
#     Name = input('What is your name? ')
#     charge = float(input('What is your charge? '))
#     payment = float(input('What is your payment? '))
#     return Name, charge, payment
#
#
# def calculate_change(charge, payment):
#     change = payment - charge
#     return change
#
#
# def find_change_in_bills(change):
#     fb = change // FIVEHUNDRED
#     hb = (change % FIVEHUNDRED) // HUNDRED
#     tb = ((change % FIVEHUNDRED) % HUNDRED) // TWENTY
#     coins = ((change % FIVEHUNDRED) % HUNDRED) % TWENTY
#     return int(fb), int(hb), int(tb), coins
#
#
# def show_change(n,c,fb,hb,tb,coins):
#     print(f'''Hello, {n}.  Thank you for visiting.
# You receive {c:.2f} Baht for change.
# You will receive {fb} 500-Baht bills, {hb} 100-Baht bills, {tb} 20-Baht bills, and {coins:.2f} Baht change in coins.''')
#
#
# Name, charge, payment = read_all_inputs()
# change = calculate_change(charge, payment)
# fb, hb, tb, coins = find_change_in_bills(change)
# show_change(Name,change,fb,hb,tb,coins)


# LAB = "turtlelab4.py"
# import urllib.request
# urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.3",LAB)
#
# from turtlelab4 import turtle,check
#
#
# def create_square(size):
#     """Commands the Turtle to create a square of the size specified"""
#
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#
#
# def create_triangle(size):
#     """Commands the Turtle to create a triangle of the size specified"""
#     turtle.forward(size)
#     turtle.left(120)
#     turtle.forward(size)
#     turtle.left(120)
#     turtle.forward(size)
#     turtle.left(120)
#
#
# create_square(100)
# create_triangle(100)
# check()


# def read_one_input(text):
#     out = input(f'Input {text} of cylinder: ')
#     return float(out)
#
#
# def get_volume(height, radius=1):
#     volume = math.pi * (radius ** 2) * height
#     return float(volume)
#
#
# def get_surface_area(height, radius=1):
#     surface_area = 2 * math.pi * radius * height + 2 * math.pi * (radius ** 2)
#     return surface_area
#
#
# def display(text, num):
#     print(f'The {text} of cylinder is {num:.3f}')
#
#
# import math
#
# radius = read_one_input("radius")
# height = read_one_input("height")
# vol = get_volume(height, radius)
# area = get_surface_area(height, radius)
# display("volume", vol)
# display("surface_area", area)


# def read_one_input(text: str) -> float:
#     out = float(input(f'Input length of {text}: '))
#     return out
#
#
# def read_multiple_inputs():
#     side1 = read_one_input('side1')
#     side2 = read_one_input('side2')
#     side3 = read_one_input('side3')
#     return side1, side2, side3
#
#
# def calculate_tri_perimeter(side1, side2, side3):
#     perimeter = (side1 + side2 + side3)
#     return perimeter
#
#
# def calculate_tri_area(perimeter, side1, side2, side3):
#     s = perimeter / 2
#     area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
#     return area
#
#
# def display_all_outputs(object: str, property1: str, value1: float, property2: str, value2: float):
#     print(f'The {property1} of {object} is {value1:.2f}')
#     print(f'The {property2} of {object} is {value2:.2f}')
#
#
# a,b,c = read_multiple_inputs()
# s = calculate_tri_perimeter(a,b,c)
# area = calculate_tri_area(s,a,b,c)
# display_all_outputs("triangle", "perimeter", s, "area", area)


# TV_PRICE = 9000
# AUDIO_PRICE = 4500
#
#
# def read_amount():
#     tvnum = int(input('Number of TVs: '))
#     aunum = int(input('Number of audio systems: '))
#     return tvnum, aunum
#
#
# def compute_total(tvnum=0, aunum=0):
#     compute = tvnum * TV_PRICE + aunum * AUDIO_PRICE
#     return compute
#
#
# def get_output_str(total=0):
#     out = 'Your total amount is {:.2f} Baht.'.format(total)
#     return out
#
#
# tvprice, audioprice = read_amount()
# total = compute_total(tvprice, audioprice)
# output_str = get_output_str(total)
# print(output_str)


# def read_vector(text:str):
#     print(text)
#     x = float(input('What is value of x? '))
#     y = float(input('What is value of y? '))
#     return x,y
#
#
# def dot_product(xA, yA, xB, yB):
#     out = float(xA)*float(xB) + float(yA)*float(yB)
#     return out
#
#
# def convert_vector_to_str(x, y):
#     return str(f'[{x:.2f}, {y:.2f}]')
#
#
# xA, yA = read_vector('For vector A')
# xB, yB = read_vector('For vector B')
# print(f'Dot product of {convert_vector_to_str(xA, yA)} and {convert_vector_to_str(xB, yB)} is {dot_product(xA, yA, xB, yB):.2f}')


# def read_vector(text: str):
#     print(text)
#     x = float(input('What is value of x? '))
#     y = float(input('What is value of y? '))
#     return x, y
#
#
# def convert_vector_to_str(x, y):
#     return str(f'[{x:.2f}, {y:.2f}]')
#
#
# def calculate(ax, ay, bx, by, choice="+"):
#     if choice == "+":
#         cx, cy = add(ax, ay, bx, by)
#     elif choice == "-":
#         cx, cy = subtract(ax, ay, bx, by)
#     return cx, cy
#
#
# def add(ax, ay, bx, by):
#     cx = ax + bx
#     cy = ay + by
#     return cx, cy
#
#
# def subtract(ax, ay, bx, by):
#     cx = ax - bx
#     cy = ay - by
#     return cx, cy
#
#
# ax, ay = read_vector("For vector A")
# bx, by = read_vector("For vector B")
# choice = input('What to do with vectors? ')
# cx, cy = calculate(ax, ay, bx, by, choice)
# print(f'[{ax:.2f}, {ay:.2f}] {choice} [{bx:.2f}, {by:.2f}] = [{cx:.2f}, {cy:.2f}]')



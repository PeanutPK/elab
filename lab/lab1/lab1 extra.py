# name1 = input("Enter name #1: ")
# gpa1 = str(input("Enter GPA #1: "))
# name2 = input("Enter name #2: ")
# gpa2 = str(input("Enter GPA #2: "))
#
# print(f"+-----------+-------+")
# print(f"|   Name    |  GPA  |")
# print(f"+-----------+-------+")
# print(f"| {name1:<7}   | {gpa1:<6}|")
# print(f"| {name2:<7}   | {gpa2:<6}|")
# print(f"+-----------+-------+")

# candy_amount = int(input('How many candies? '))
# friend_amount = int(input('How many friends? '))
# print(f'There are {candy_amount} candies shared between {friend_amount} friends.')
# print(f'Each friend will obtain {candy_amount//friend_amount} candies.')
# print(f'{candy_amount%friend_amount} candies are not shared between friends.')

# w = float(input('Input width? '))
# l = float(input('Input length? '))
# a = w * l
# amount_of_land_sell = a // 100
# print(f'The landlord will have {int(amount_of_land_sell)} pieces of land available for sale.')
# print(f'He will earn {int(amount_of_land_sell*1600)} pounds from the sale.')

# b = float(input('Input base? '))
# h = float(input('Input height? '))
# print(f'For triangle with base={b:.3f} and height={h:.3f}, area is {0.5*h*b:.3f}.')

# x = float(input('Input x? '))
# y = float(input('Input y? '))
# formula = (((x-y)/(x+y))*(3.14/(0.15+(y/x))))
# print(f'The result value is {formula:.5f}')

name = input('Input your name? ')
birth_year = int(input('Input your birthyear? '))
current_year = int(input('Input current year? '))
print(f'Welcome, {name}')
print(f'Currently, you are {current_year-birth_year} years old.')

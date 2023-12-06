# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print(i + 1, end='')


# def w_to_bmi(w, h):
#     h /= 100
#     bmi = w / (h * h)
#     return bmi
#
#
# def is_bmi(b):
#     if b < 18.5:
#         print('You are underweight.')
#     elif b < 25:
#         print('You are normal.')
#     elif b < 30:
#         print('You are overweight.')
#     else:
#         print('You are obese.')
#
#
# weight = float(input('Enter your weight in kg: '))
# height = float(input('Enter your height in cm: '))
# bmi = w_to_bmi(weight, height)
# print(f'Your BMI is {bmi:.2f}.')
# is_bmi(bmi)


# def percent_to_score():
#     hw = float(input('Enter your homework percent: ')) * 0.1
#     mt = float(input('Enter your midterm percent: ')) * 0.4
#     fn = float(input('Enter your final percent: ')) * 0.5
#     scores = hw + mt + fn
#     return scores
#
#
# def score_to_grade(scores):
#     if 0 <= scores < 50:
#         g = 'F'
#     elif scores < 55:
#         g = 'D'
#     elif scores < 60:
#         g = 'D+'
#     elif scores < 65:
#         g = 'C'
#     elif scores < 70:
#         g = 'C+'
#     elif scores < 75:
#         g = 'B'
#     elif scores < 80:
#         g = 'B+'
#     else:
#         g = 'A'
#     print(f'Your grade is {g}.')
#
#
# score = percent_to_score()
# print(f'Your total score is {score:.2f}.')
# score_to_grade(score)


AD = int(input('Enter year in AD: '))
if AD <= 0:
    print('Invalid input: use positive integer')
elif AD < 1752 and AD % 4 == 0:
    print(f'AD {AD} is a leap year')
elif ((AD % 4 == 0 and AD % 100 != 0) or AD % 400 == 0) and AD > 0:
    print(f'AD {AD} is a leap year')
else:
    print(f'AD {AD} is not a leap year')


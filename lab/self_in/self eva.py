# from math import ceil
#
#
# def calculate_total_volume(guests, volumes):
#     guests = int(guests)
#     volumes = float(volumes)
#     return guests * volumes
#
#
# def find_exact_num_bottles(total_volume):
#     bot_num = total_volume / LITERTOOUNCES
#     return bot_num
#
#
# LITERTOOUNCES = 33.814
# guest = input('Enter number of guests: ')
# volume = input('Enter glass volume: ')
# total = calculate_total_volume(guest, volume)
# bottle = find_exact_num_bottles(total)
# print(f'Soda\'s exactly required {bottle:.2f} 2-liter bottles.')
# print(f'Hence, you must purchase at least {ceil(bottle)} 2-liter bottles.')


from math import ceil

weight_lose = float(input('Enter weight you want to lose (kg.): '))
running_distance = float(input('Enter distance you run per day (km): '))

run_day = int(ceil((weight_lose*7700)/(running_distance*60)))
run_distance = (weight_lose*7700)/60

print(f'You should run {run_distance:.2f} kilometers to lose {weight_lose:.2f} kilograms.')
print(f'You will spend {run_day} days for running.')


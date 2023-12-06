# floor3_rooms = {'4/4': 1, '4/5': 2, '5/1': 3, '5/2': 4, '5/3': 5}
# classroom_floors = {room: 'floor3' for room in floor3_rooms}
# print(classroom_floors)
#
# class4_year_rooms = {room: 'year4' for room in classroom_floors if
#                      room[0] == '4'}
# class5_year_rooms = {room: 'year5' for room in classroom_floors if
#                      room[0] == '5'}
# print(class4_year_rooms)
# print(class5_year_rooms)
#
# left_wings = {room_num: room for room, room_num in floor3_rooms.items() if
#               room_num < 4}
# right_wings = {room_num: room for room, room_num in floor3_rooms.items() if
#                room_num > 3}
# print(left_wings)
# print(right_wings)

x = [1, 2, 3, 4]
y = {1: 'yi', 2: 'er', 3: 'san', 4: 'si'}
for i in y:
    print(i)

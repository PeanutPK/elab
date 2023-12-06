fruit_price = {'apple': 20, 'banana': 10, 'orange': 5, 'melon': 15}
fruit_basket = ['apple', 'banana', 'orange', 'melon']


def fruit1():
    def read_fruits(fruit_basket):
        _dic = {}
        word = input('Enter choice or quit: ')
        while word != 'quit':
            if word in fruit_basket:
                name = input('Enter name: ')
                _dic[name] = word
            else:
                print('Your fruit choice is not available.')
            word = input('Enter choice or quit: ')
        return _dic

    def print_price(fruit_price, choice_dict):
        for i in choice_dict:
            print(f'{i} pays {fruit_price.get(choice_dict[i]):.2f} Baht')

    def compute_total_price(fruit_price, choice_dict):
        _sum = 0
        for i in choice_dict.values():
            _sum += fruit_price.get(i)
        return _sum

    def find_min_price(fruit_price, choice_dict):
        price = 'No one pays the least'
        _min = float('inf')
        _count = 0
        for k, i in choice_dict.items():
            if _min >= fruit_price.get(i):
                price = f"{k} pays the least = {fruit_price.get(i):.2f} Baht"
                _min = fruit_price.get(i)
        return price

    def fruitTest():
        _dic = read_fruits(fruit_price)
        print(_dic)
        print_price(fruit_price, _dic)
        total = compute_total_price(fruit_price, _dic)
        print(f'Total price = {total:.2f} Baht')
        print(find_min_price(fruit_price, _dic))


def fruit2():
    # Input name and fruit
    _list = []
    choice = input('Enter name or quit: ')
    while choice != 'quit':
        fruit = input('Enter fruit: ')
        while fruit not in fruit_basket:
            print('Your fruit choice is not available.')
            fruit = input('Enter fruit: ')
        _list.append({'name': choice, 'fruit': fruit})
        choice = input('Enter name or quit: ')
    print(_list)

    # change fruit according to name
    def changeFruit():
        name = input('Enter name: ')
        new_fruit = input('Enter new fruit choice: ')
        while new_fruit not in fruit_basket:
            print('Your fruit choice is not available.')
            new_fruit = input('Enter new fruit choice: ')
        for i in _list:
            if i['name'] == name:
                i['fruit'] = new_fruit
        print(_list)

    # search people who buy fruit monkey way
    def monkeySearch():
        search = input('Enter search fruit: ')
        while search not in fruit_basket:
            print('Your fruit choice is not available.')
            search = input('Enter search fruit: ')
        print(f'People who order {search}: ', end='')
        count = 0
        for i in _list:
            if search in i['fruit']:
                print(i['name'], end=', ')
                count += 1
        if count == 0:
            print('No one')


def buggedFood():
    def read_one_room(fruit_basket):
        _list = []
        choice = input('Enter choice or quit: ')
        while choice != 'quit':
            if choice not in fruit_basket:
                print('Your fruit choice is not available.')
            else:
                _list.append(choice)
            choice = input('Enter choice or quit: ')
        return _list

    def count_fruit(room_choices, search_fruit):
        search = {k: v.count(search_fruit) for k, v in room_choices.items()}
        return search

    def order(_dic):
        for k, v in _dic.items():
            print(f'{k} orders {v}.')

    _dic = {}
    n = int(input('Enter #rooms: '))
    for i in range(1, n + 1):
        print(f'Room{i}')
        _dic[f'Room{i}'] = read_one_room(fruit_basket)
    print(_dic)
    room = int(input('Enter room to removed: '))
    print('After remove')
    _dic.pop(f'Room{room}')
    print(_dic)
    _count = input('Enter fruit to count: ')
    print(count_fruit(_dic, _count))


weeks = [[0, 0, 0, 1, 2, 3, 4],

         [5, 6, 7, 8, 9, 10, 11],

         [12, 13, 14, 15, 16, 17, 18],

         [19, 20, 21, 22, 23, 24, 25],

         [26, 27, 28, 29, 30, 0, 0]]

days_in_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_weeks = len(weeks)

month_dict = {}
for i in range(0, num_weeks):
    week_dict = {}
    for j in range(0, 7):
        week_dict[days_in_week[j]] = weeks[i][j]
    month_dict[f'Week{i + 1}'] = week_dict
    print(week_dict)
print(month_dict)

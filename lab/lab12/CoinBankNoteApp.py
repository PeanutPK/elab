class Coin:
    def __init__(self, value=1):
        self.v = value

    def __str__(self):
        return f"{self.v} Baht Coin"

    def get_value(self):
        return self.v

    def set_value(self, value=1):
        self.v = value
        return Coin(self.v)


class Banknote:
    def __init__(self, value=20):
        self.v = value

    def __str__(self):
        return f"{self.v} Baht Banknote"

    def get_value(self):
        return self.v

    def set_value(self, value=20):
        self.v = value


amount = int(input('Input amount : '))
moneys = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
if amount > 0:
    for money in moneys:
        if amount >= money:
            n = amount // money
            amount %= money
            if money > 10:
                print(f'You get {n} of {Banknote(money)}')
            else:
                print(f'You get {n} of {Coin(money)}')


# while amount > 0:
#     if amount // 1000 > 0:
#         n = amount // 1000
#         amount %= 1000
#         print(f'You get {n} of {Banknote(1000)}')
#     elif amount // 500 > 0:
#         n = amount // 500
#         amount %= 500
#         print(f'You get {n} of {Banknote(500)}')
#     elif amount // 100 > 0:
#         n = amount // 100
#         amount %= 100
#         print(f'You get {n} of {Banknote(100)}')
#     elif amount // 50 > 0:
#         n = amount // 50
#         amount %= 50
#         print(f'You get {n} of {Banknote(50)}')
#     elif amount // 20 > 0:
#         n = amount // 20
#         amount %= 20
#         print(f'You get {n} of {Banknote(20)}')
#     elif amount // 10 > 0:
#         n = amount // 10
#         amount %= 10
#         print(f'You get {n} of {Coin(10)}')
#     elif amount // 5 > 0:
#         n = amount // 5
#         amount %= 5
#         print(f'You get {n} of {Coin(5)}')
#     elif amount // 2 > 0:
#         n = amount // 2
#         amount %= 2
#         print(f'You get {n} of {Coin(2)}')
#     elif amount // 1 > 0:
#         n = amount // 1
#         amount %= 1
#         print(f'You get {n} of {Coin(1)}')

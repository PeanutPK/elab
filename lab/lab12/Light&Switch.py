class Switch:
    def __init__(self, name='', status=False):
        self.n = name
        self.st = status

    def turn(self):
        self.st = not self.st

    def clone(self):
        return Switch(self.n + '.copy', self.st)

    def __str__(self):
        stat = 'off'
        if self.st:
            stat = 'on'
        return f"switch({self.n}) is {stat}"


class Light:
    def __init__(self, name='', switch=Switch()):
        self.n = name
        self.sw = switch

    def turn(self):
        self.sw.st = not self.sw.st

    def get_status(self):
        stat = 'off'
        if self.sw.st:
            stat = 'on'
        return stat

    def set_switch(self, new_switch):
        self.sw = new_switch

    def clone(self):
        return Light(self.n + '.copy', self.sw.clone())

    def __str__(self):
        return f"light({self.n}) with switch({self.sw.n}) is {self.get_status()}"


# Create a switch and a light
s1 = Switch("switch1")
light1 = Light("light1", s1)

# Test the methods
print(s1)  # Output: switch(switch1) is off
print(light1)  # Output: light(light1) with switch(switch1) is off

s1.turn()  # Turn the switch on
print(s1)  # Output: switch(switch1) is on
print(light1)  # Output: light(light1) with switch(switch1) is on

light1.turn()  # Turn the light off
print(s1)  # Output: switch(switch1) is on
print(light1)  # Output: light(light1) with switch(switch1) is off

s1_copy = s1.clone()  # Clone the switch
print(s1_copy)  # Output: switch(switch1.copy) is on

light1_copy = light1.clone()  # Clone the light
print(
    light1_copy)  # Output: light(light1.copy) with switch(switch1.copy) is off

new_switch = Switch("switch2", True)
light1.set_switch(new_switch)
print(light1)  # Output: light(light1) with switch(switch2) is on

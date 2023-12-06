class Switch:
    def __init__(self, name, status=False):
        self.name = name
        self.status = status

    def turn(self):
        self.status = not self.status

    def clone(self):
        return Switch(self.name + ".copy", self.status)

    def __str__(self):
        return f"switch({self.name}) is {'on' if self.status else 'off'}"


class Light:
    def __init__(self, name, switch):
        self.name = name
        self.switch = switch

    def turn(self):
        self.switch.turn()

    def get_status(self):
        return "on" if self.switch.status else "off"

    def set_switch(self, new_switch):
        self.switch = new_switch

    def clone(self):
        cloned_switch = self.switch.clone()
        return Light(self.name + ".copy", cloned_switch)

    def __str__(self):
        return f"light({self.name}) with switch({self.switch.name}) is {self.get_status()}"


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

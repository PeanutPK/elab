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


class Person:
    def __init__(self, _id='', name='', l_name='', gender='', age=0):
        self.i = _id
        self.n = name
        self.L = l_name
        self.g = gender
        self.a = age

    def __str__(self):
        return f"{self.i}, {self.n} {self.L}, {self.g}, {self.a}"

    def set_id(self, _id=''):
        self.i = _id

    def get_id(self):
        return self.i

    def get_name(self):
        return self.n

    def set_name(self, name=''):
        self.n = name

    def get_lastname(self):
        return self.L

    def set_lastname(self, l_name=''):
        self.L = l_name

    def get_gender(self):
        return self.g

    def set_gender(self, gender=''):
        self.g = gender

    def get_age(self):
        return self.a

    def set_age(self, age=0):
        self.a = age


class Location:
    def __init__(self, room='', floor=0):
        self.p = ''
        self.r = room
        self.f = floor

    def __str__(self):
        if self.p == '':
            _str = f"{self.r} on floor {self.f}. No one is in this room."
        else:
            _str = f"{self.r} on floor {self.f}. {self.p} is in this room."
        return _str

    def get_person(self):
        return self.p

    def set_person(self, person=''):
        self.p = person

    def get_room(self):
        return self.r

    def set_room(self, room=''):
        self.r = room

    def get_floor(self):
        return self.f

    def set_floor(self, floor=0):
        self.f = floor


class Radio:
    def __init__(self):
        self.m = 'FM'
        self.f = 87.5

    def set_mode(self, mode):
        self.m = mode
        if mode == 'AM':
            self.f = 150
        else:
            self.f = 87.5

    def set_frequency(self, frequency):
        if self.m == 'FM':
            if 87.5 <= frequency <= 108:
                self.f = frequency
        else:
            if 150 <= frequency <= 280:
                self.f = frequency
        return self.f

    def adjust_frequency(self, frequency):
        if self.m == 'FM':
            if 87.5 <= self.f + frequency <= 108:
                self.f += frequency
                return True
        else:
            if 150 <= self.f + frequency <= 280:
                self.f += frequency
                return True
        return False

    def __str__(self):
        if self.m == 'FM':
            return f"{self.m} Radio: {self.f:.1f} MHz"
        return f"{self.m} Radio: {self.f:.1f} kHz"

    def get_mode(self):
        return self.m

    def get_frequency(self):
        return self.f


class Car:
    def __init__(self, gas=0, burning_gas_rate=0):
        self.g = gas
        self.b = burning_gas_rate

    def drive(self, distance):
        used_gas = (distance / self.b)
        self.g -= used_gas
        return self.g

    def fill_gas(self, new_gas):
        self.g += new_gas

    def __str__(self):
        return f"Gas: {self.g}, Burning rate: {self.b}"

    def get_gas(self):
        return self.g

    def get_burning_rate(self):
        return self.b

    def set_gas(self, gas=0):
        self.g = gas

    def set_burning_rate(self, burning_gas_rate=0):
        self.b = burning_gas_rate


class ClassRoom:
    def __init__(self, grade=0, homeRoomTeacher='', studentList=[],
                 numStudents=0):
        self.g = grade
        self.h = homeRoomTeacher
        self.s = studentList
        self.n = numStudents

    def get_student_no(self, n):
        if n - 1 < 10:
            return self.s[n]

    def add_student(self, student_name):
        if len(self.s) < 10:
            self.s.append(student_name)
            return True
        return False

    def change_student(self, n, new_name):
        if n - 1 > 0:
            self.s[n - 1] = new_name
            return True
        return False

    def remove_student(self, student_name):
        if student_name in self.s:
            self.s.remove(student_name)
            return True
        return False

    def remove_student_no(self, n):
        if len(self.n):
            self.s.pop(n)
            return True
        return False

    def __str__(self):
        return (f"Grade: {self.g}\n"
                f"Homeroom Teacher: {self.h}\n"
                f"Students: {', '.join(self.s)}")

    def set_grade(self, grade):
        self.g = grade

    def set_homeroom_teacher(self, homeroom_teacher):
        self.h = homeroom_teacher

    def set_student_list(self, student_list):
        self.s = student_list

    def set_num_student(self, num_student):
        self.n = num_student

    def get_grade(self):
        return self.g

    def get_homeroom_teacher(self):
        return self.h

    def get_student_list(self):
        return self.s

    def get_num_student(self):
        return self.n


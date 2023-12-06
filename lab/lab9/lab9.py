def fah_to_cel(start, stop, step):
    print(f"{'Fahrenheit':>12}{'Celcius':>12}")
    print(f"{'----------':>12}{'-------':>12}")
    fah = start
    while fah != stop:
        if (step < 0 and fah < stop) or (step > 0 and fah > stop):
            break
        cel = (fah - 32) * 5 / 9
        print(f'{fah:>12.2f}{cel:>12.2f}')
        fah += step
    print(f"{'----------':>12}{'-------':>12}")


def printSleepTime(start_time, duration):
    """
    Print sleeping time starting from start_time and lasting for duration minutes
    :params start_time: time to start sleeping
            duration: duration of sleeping
    >>> printSleepTime(1,5)
    1 min
    2 min
    3 min
    4 min
    5 min
    >>> printSleepTime(6,2)
    6 min
    7 min
    >>> printSleepTime(11,3)
    11 min
    12 min
    13 min
    """
    for i in range(duration):
        print(f'{i + start_time} min')


def nap_main():
    nap_time = int(input("Input nap time: "))
    snooze_time = int(input("Input snooze time: "))

    print('Nap time starts.')
    printSleepTime(1, nap_time)
    wake = input('Alarm rings. Dismiss or Snooze: ')
    while wake != 'Dismiss':
        printSleepTime(nap_time + 1, snooze_time)
        wake = input('Alarm rings. Dismiss or Snooze: ')
        nap_time += snooze_time


def turtle_leap():
    H = int(input("What is the well's depth? "))
    U = int(input("Enter the height the frog can jump up: "))
    D = int(input("Enter the height the frog slips down: "))
    day = 1
    if U != D or H == U == D:
        while H - U > 0:
            print(f"On day {day} the frog leaps to the depth of {H - U} meters.\n"
                  f"At night he slips down to the depth of {H - U + D} meters.")
            day += 1
            H = H - U + D
        print(f"The frog gets out of the well on day {day}.")
    else:
        print("The frog will never escape from the well.")


LAB = "turtlelab8.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtle.turtlelab8 import check

# Put your turtle movement commands here
# ______________________________________
# ______________________________________
# ______________________________________

check()


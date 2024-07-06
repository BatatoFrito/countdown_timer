"""

This program is a countdown timer in the terminal

"""

import time
import os

def clear():
    return os.system('cls')

def sleep(seconds: float):
    return time.sleep(seconds) 

def countdown(time: int):
    clear()
    if time == 0:
        print(f"{time}\nTime's up!")
        return
    else:
        print(time)
    sleep(1)
    time -= 1
    countdown(time)

countdown(10)

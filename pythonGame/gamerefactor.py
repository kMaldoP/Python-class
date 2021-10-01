
import random
from my_pkg.midday_module import big_tipper, cartow, catch_Happy_hour, flat_tire, rando_venmo, walk_out
from my_pkg.morning_module import total, Avo_toast, smoothie, burrito, coffee, energy_drink, eat_at_work
from my_pkg.afternoon_module import *

class MakeChoice:
    def __init__(self, total, choice):
        self.total = total
        self.choice = choice
        

def choose(self, choice):
    choice = input(" are you going to work today?")
    while True:
        if choice == 1 or choice == "1":
            morning_list = [Avo_toast, smoothie, burrito]
            random.choice(morning_list)()
            break
        elif choice == 2 or choice == "2":
            morning_list_no = [coffee, energy_drink, eat_at_work]
            random.choice(morning_list_no)()
            break

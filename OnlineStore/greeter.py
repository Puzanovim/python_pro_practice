from datetime import datetime


def _get_day():
    return datetime.now().strftime("%A")


def _get_part_of_day():
    current_hour = datetime.now().hour

    if current_hour < 12:
        part_of_day = "morning"
    elif current_hour < 17:
        part_of_day = "afternoon"
    else:
        part_of_day = "evening"

    return part_of_day


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, store):
        day = _get_day()
        part_of_day = _get_part_of_day()
        print(f"Hello, my name is {self.name}.\n"
              f"Welcome to {store}!\n"
              f"Have a nice {day} {part_of_day}\n"
              f"Give you a discount coupon on 20%")

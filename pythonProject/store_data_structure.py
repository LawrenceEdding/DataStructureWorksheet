import random

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')


def store_months():
    month_with_pi = months[2]
    return month_with_pi


def birthday_locations():
    celebration_location = {'Dave n Busters', 'Home', 'Florida', 'Mount Rushmore'}
    celebration_location.add({'Washington DC', 'Great lakes', 'JJ\'s Diner'})
    for i in celebration_location:
        print(i)


def sweepstakes():
    contestants = [{"name": "Ryan Moore"}, {"name": "John Gossler"}, {"name": "Simone Whittaker"},
                   {"name": "Patrice Ender"}, {"name": "Zoom Cloud"}]
    print(f'{contestants[random.randint(0, 4)]["name"]} has won')


def family():
    family_list = [{"fname": "John", "lname": "Warrior", "relation": "Father"},
                   {"fname": "Zach", "lname": "Warrior", "relation": "Brother"},
                   {"fname": "Alice", "lname": "Warrior", "relation": "Sister"},
                   {"fname": "Mary", "lname": "Warrior", "relation": "Mother"}]
    print(f'{family_list}')

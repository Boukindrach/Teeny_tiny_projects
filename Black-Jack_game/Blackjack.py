#!/usr/bin/python3

import random

Money = 5000
g = 0
total = 0
print("You have {}$:\nHow much to bet from it?".format(Money))
bet = input()

print("Your bet is {}".format(bet))

def cards(type_card, number_card):
    number_card = random.randint(1, 13)
    type_card = random.randint(0, 4)
    if type_card == 1:
        type_card = chr(9829)
    elif type_card == 2:
        type_card = chr(9830)
    elif type_card == 3:
        type_card = chr(9824)
    else:
        type_card = chr(9827)

    if number_card == 11:
        number_card = "J"
    elif number_card == 12:
        number_card = "Q"
    elif number_card == 13:
        number_card = "K"

    return type_card, number_card

type_ = ""
number_ = 0
first_card = cards(type_, number_)
if isinstance(first_card[1], int):
    total += first_card[1]
else:
    total += 10
print("""
┌─────────┐     ┌─────────┐
| {}       |     |         |
|         |     |         |
|    {}    |     |         |
|         |     |         |
|      {}  |     |         |
└─────────┘     └─────────┘
""".format(first_card[1], first_card[0], first_card[1]))
print(first_card[0], first_card[1], total)

if player_count > 21:
    print("you lost, dealer win")
if Dealer_count > 21:
    print("you win, dealer lost")

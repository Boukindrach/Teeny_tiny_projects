#!/usr/bin/python3

import random

cards = random.randint(1, 13)
Money = 5000
g = ''
h = ''
print("You have {}$:\nHow much to bet from it?".format(Money))
bet = input()

print("Your bet is {}".format(bet))

for j in range(0, 3):
    if j == 0 or j == 2:
        print("Dealer:".format(j))
    else:
        print("Player:")
    x = random.randint(1, 13)
    y = random.randint(1, 13)
    if x >= 11:
        if x == 11:
            x = "J"
        if x == 12:
            x = "Q"
        else:
            x == "K"

    type_card = random.randint(1, 4)
    if type_card == 1:
        g = chr(9829)
    elif type_card == 2:
        g = chr(9830)
    elif type_card == 3:
        g = chr(9824)
    else:
        g = chr(9827)
    if j <= 1:
        if y >= 11:
            if y == 11:
                y = "j"
            if y == 12:
                y = "Q"
            else:
                y == "K"

        type_card = random.randint(1, 4)
        if type_card == 1:
            h = chr(9829)
        elif type_card == 2:
            h = chr(9830)
        elif type_card == 3:
            h = chr(9824)
        else:
            h = chr(9827)

    print("{} {} : {} {}".format(x, g, y, h))


#!/usr/bin/python3
"""Bagels a logic deductive game Where you must guess a number based on clues.
    for the book Big book for small python Projects"""

import random


print ("""Hello and Welcome to the Bagels.
Where I will be thinking about a number of 3 digits and you will try to guess what it is.
Here is the rules:

When I say:     That means:
    Pico            One digit is correct but in the wrong position
    Fremi           One digit is correct and in the right position
    Bagels          No digit is correct """)

random_number = str(random.randint(000, 999))
for x in range(0, 10):
    print("Guess #{}".format(x))
    x = input()
    a = 1
    if x == random_number:
        print("You Got It!!!")
        break
    for j in range(0, 3):
        for i in range(0, 3):
            if x[i] == random_number[j]:
                if i == j:
                    print ("Fermi", end=" ")
                else:
                    print ("Pico", end=" ")
            else:
                a += 1
                if a == 10:
                    print("Bagels")
    print(random_number)
    if x == 9:
        print("time is out, try again next time")

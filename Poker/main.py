import random
import numpy as np
from matplotlib import pyplot as plt

# Befüllung eines Kartendecks mit 52 Karten aus 4 verschiedenen Farben
karten = list(range(0, 52))

kombinationen = {"royal_flush": 0,
                 "straight_flush": 0,
                 "vierling": 0,
                 "full_house": 0,
                 "flush": 0,
                 "strasse": 0,
                 "drilling": 0,
                 "zwei_paare": 0,
                 "paar": 0,
                 "high_card": 0}


def play(anzahl):
    for i in range(anzahl):
        stopper = False

        hand = random.sample(karten, 5)

        main_shema, main_color_shema = check(hand)
        while not stopper:
            stopper = royal_flush(main_shema, main_color_shema)
            stopper = straight_flush(main_shema, main_color_shema)
            stopper = vierling(main_shema, main_color_shema)
            stopper = full_house(main_shema)
            stopper = flush(main_shema, main_color_shema)
            stopper = strasse(main_shema, main_color_shema)
            stopper = drilling(main_shema)
            stopper = zwei_paare()
            stopper = paar(main_shema)


def check(hand):
    modulo_12_values = []
    colors = []
    for num in hand:
        modulo_value = num % 12
        modulo_12_values.append(modulo_value)
        colors.append(num // 12)
    return modulo_12_values, colors


def royal_flush(hand, farbe):
    shema = [8, 9, 10, 11, 12]
    farben = ([1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [4, 4, 4, 4])

    if hand in shema and farbe in farben:
        kombinationen["royal_flush"] += 1
        return True


def straight_flush(hand, farbe):
    farben = ([1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [4, 4, 4, 4])

    sorted = hand.sort()

    if hand == sorted and farbe in farben:
        kombinationen["straight_flush"] += 1
        return True


def vierling(hand, farbe):
    if hand[0] == hand[1] == hand[2] == hand[4]:
        if farbe.sort() == [1, 2, 3, 4]:
            kombinationen["vierling"] += 1
            return True


def paar(hand):
    if (x for x in hand if hand.count(x) == 2):
        kombinationen["paar"] += 1
        return True


def drilling(hand):
    if (x for x in hand if hand.count(x) == 3):
        kombinationen["drilling"] += 1
        return True


# prio
def full_house(hand):
    if (x for x in hand if hand.count(x) == 3):
        if (x for x in hand if hand.count(x) == 2):
            kombinationen["full_house"] += 1
            return True


def flush(hand, farbe):
    farben = ([1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [4, 4, 4, 4])
    if farbe in farben:
        if hand != hand.sort():
            kombinationen["flush"] += 1
            return True


def strasse(hand, farbe):
    farben = ([1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [4, 4, 4, 4])
    if farbe in farben:
        if hand == hand.sort():
            kombinationen["strasse"] += 1
            return True


def zwei_paare():
    kombinationen["zwei_paare"] += 1
    return True


if __name__ == '__main__':
    play(10000)
    print(kombinationen)

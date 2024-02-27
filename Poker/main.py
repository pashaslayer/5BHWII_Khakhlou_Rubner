import random
import sys
import time

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


# Time decorator
def timeit(method):
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()

        print(f"{method.__name__} took {end_time - start_time:.3f} seconds to execute")
        return result

    return timed


def play(anzahl):
    for i in range(anzahl):
        hand = random.sample(karten, 5)
        main_shema, main_color_shema = check(hand)

        if royal_flush(main_shema, main_color_shema):
            kombinationen["royal_flush"] += 1
        elif straight_flush(main_shema, main_color_shema):
            kombinationen["straight_flush"] += 1
        elif vierling(main_shema):
            kombinationen["vierling"] += 1
        elif full_house(main_shema):
            kombinationen["full_house"] += 1
        elif flush(main_color_shema):
            kombinationen["flush"] += 1
        elif strasse(main_shema):
            kombinationen["strasse"] += 1
        elif drilling(main_shema):
            kombinationen["drilling"] += 1
        elif zwei_paare(main_shema):
            kombinationen["zwei_paare"] += 1
        elif paar(main_shema):
            kombinationen["paar"] += 1
        else:
            kombinationen["high_card"] += 1


def check(hand):
    modulo_13_values = [num % 13 for num in hand]
    colors = [num // 13 for num in hand]
    return modulo_13_values, colors


def royal_flush(hand, farbe):
    shema = [8, 9, 10, 11, 12]

    if len(set(farbe)) == 1:
        return set(hand) == set(shema)

    return False


def straight_flush(hand, farbe):
    if len(set(farbe)) == 1:
        return sorted(hand) == list(range(min(hand), max(hand) + 1))

    return False


def vierling(hand):
    return hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]


def paar(hand):
    for x in hand:
        if hand.count(x) == 2:
            return True
    return False


def drilling(hand):
    for x in hand:
        if hand.count(x) == 3:
            return True
    return False


def full_house(hand):
    return drilling(hand) and paar(hand)


def flush(farbe):
    return len(set(farbe)) == 1


def strasse(hand):
    return sorted(hand) == hand and len(set(hand)) == 5


def zwei_paare(hand):
    count_pairs = 0
    for x in set(hand):
        if hand.count(x) == 2:
            count_pairs += 1
    return count_pairs == 2


def calculate_percentage(combination_count, total):
    percentages = {key: value / total * 100 for key, value in combination_count.items()}
    return percentages


if __name__ == '__main__':
    # total_games = 1000000
    total_games = int(sys.argv[1])
    play(total_games)

    print(kombinationen)
    percentages = calculate_percentage(kombinationen, total_games)

    # Ausdrucken der prozentualen Anteile
    for key, value in percentages.items():
        print(f"{key}: {value}%")

import random as rdm

zahlen_geraten = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0
}


def play():
    a = [x for x in range(10)]

    pck = rdm.choice(a)
    rand_pick = rdm.randint(0, 10)

    if pck == rand_pick:
        print(f"You picked the right number! [Your pick: {pck} --- Computer pick: {rand_pick}]")
        print()
        zahlen_geraten[str(pck)] += 1

    else:
        print(f"WRONG NUMBER: [Your pick: {pck} --- Computer pick: {rand_pick}]")


def show_stats():
    print(zahlen_geraten)

def make_string(s):
    print("".join(x[0] for x in s.split(" ")))

if __name__ == '__main__':
    make_string("hello dff dff")
    make_string("hello")

    while True:
        while True:
            play()

            if input("Stop? Y/N").lower() == "y":
                break

        if input("Show stats: [press s]").lower() == "s":
            show_stats()

        else:
            break

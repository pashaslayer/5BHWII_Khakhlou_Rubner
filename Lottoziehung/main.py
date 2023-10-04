import random


zahlen = list(range(1, 46))
ran_num = []


def lotto_ziehung():

    random_number = random.sample(zahlen, 1)
    ran_num.append(random_number)


if __name__ == '__main__':
    lotto_ziehung()
    lotto_ziehung()
    lotto_ziehung()
    lotto_ziehung()
    lotto_ziehung()
    lotto_ziehung()

    for i in ran_num:
        print("Number: ")
        print(i)
        print("\n")



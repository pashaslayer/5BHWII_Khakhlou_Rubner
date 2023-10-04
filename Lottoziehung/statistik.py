import random
import matplotlib.pyplot as plt

random_numbers = []

if __name__ == '__main__':
    for i in range(1000):
        random_numbers.append(random.randint(1, 45))

    plt.hist(random_numbers, bins=range(1, 47), align='left', rwidth=0.9, alpha=0.7)
    plt.xticks(range(1, 46), rotation=60)
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.title('Frquency of random selected numbers from 1 to 45')
    plt.show()

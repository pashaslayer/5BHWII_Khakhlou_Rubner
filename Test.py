class Shop:
    def __init__(self, shopname):
        self.shopname = shopname
        self.animals = []


class Animal:
    def __init__(self, name, age, price):
        self.name = name
        self.age = age
        self.price = price

    def __str__(self):
        return f"Name : {self.name} - Age : {self.age} - Price : {self.price}"


class Dog(Animal):
    def __init__(self, name, age, price, noise):
        super().__init__(name, age, price)
        self.noise = noise

    def __str__(self):
        return super().__str__() + f" - Noise : {self.noise}"


class Parrot(Animal):
    def __init__(self, name, age, price, color):
        super().__init__(name, age, price)
        self.color = color

    def __str__(self):
        return super().__str__() + f" - Color : {self.color}"


if __name__ == '__main__':
    # Anlegen eines Shops für den Verkauf von Tieren
    shop = Shop("Animal Farm")

    dog_ben = Dog("Ben", 4, 250.99, "woof woof")
    dog_pascal = Dog("Pascal", 0.2, 950.55, "wu wu wu")

    parrot_karry = Parrot("Karry", 1.2, 15.00, "yellow-green")
    parrot_parry = Parrot("Parry", 2.5, 2500.90, "exotic-purple")
    parrot_husky = Parrot("Husky", 6.2, 344.60, "blue-red")

    shop.animals.append(dog_ben)
    shop.animals.append(dog_pascal)
    shop.animals.append(parrot_husky)
    shop.animals.append(parrot_parry)
    shop.animals.append(parrot_karry)

    animals = [str(x) for x in shop.animals]
    print(animals)

    print(dog_pascal)
    print(Dog.__mro__)



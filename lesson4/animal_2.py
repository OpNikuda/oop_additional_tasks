"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'



class Dog(Animal):
    def bark(self):
        print('Bark!')

    def speak(self):
        self.bark()


class Cat(Animal):

    def meow(self):
        print('Meow!')

    def speak(self):
        return f'{self.meow()}'



animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    print(animal)
    animal.speak()

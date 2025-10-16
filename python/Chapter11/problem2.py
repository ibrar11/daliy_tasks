class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    def bark(self):
        print("Woooof!")

dog = Dog()
dog.bark()
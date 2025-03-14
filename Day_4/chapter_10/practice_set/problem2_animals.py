class Animals:
    pass

class Pet(Animals):
    pass

class Dog(Pet):
    @staticmethod
    def bark():
        print("BOW BOW ")


a = Dog()
a.bark()
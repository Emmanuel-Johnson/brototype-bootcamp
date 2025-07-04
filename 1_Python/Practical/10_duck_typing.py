# Duck Typing

class Dog:
    def sound(self):
        print("Woof!")
    def move(self):
        print("Running on four legs.")

class Cat:
    def sound(self):
        print("Meow!")
    def move(self):
        print("Prowling silently.")

def animal_actions(animal):
    animal.sound()
    animal.move()

dog_instance = Dog()
cat_instance = Cat()

animal_actions(dog_instance)
animal_actions(cat_instance)
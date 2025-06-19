# Duck typing is a concept in Python that focuses on an object's behavior rather than its specific type.
# It's based on the idea that if an object "walks like a duck and quacks like a duck," it can be treated as a duck, 
# regardless of its actual class or inheritance.

# In Python, duck typing means that the type or class of an object is less important than the methods and properties it defines.
# Instead of checking the type of an object, Python checks whether the object has the required methods and attributes.

# For example, if a function expects an object with a walk() method, it will work with any object that has a walk() method, 
# regardless of whether it's a Duck object or not. This allows for more flexible and reusable code.

# Here's a simple example:

class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

def make_sound(animal):
    animal.quack()

duck = Duck()
dog = Dog()

make_sound(duck) # Output: Quack!
make_sound(dog)  # Output: Woof!

# In this example, both the Duck and Dog classes have a quack() method, so both can be passed to the make_sound function, 
# even though they are different classes.

# Duck typing makes Python more dynamic, flexible, and easier to use, as it allows for polymorphism without explicit type declarations.

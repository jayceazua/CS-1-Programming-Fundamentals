class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

# adding two subclasses -  they inherit from their superclass

class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs




# Question on OOP:
# Q 1: What is a 'class'? What is an example of a class besides pets and dogs and cats
# A 1: A class is a blueprint of an object with methods and attributes.
class Car(object):
    def __init__(self, make, modal, wheels):
        self.make = make
        self.modal = modal
        self.wheels = 4

# Q 2: How are classes used in OOP?
# A 2: Classes are used as reusable code to create instances of the class easily.
# Q 3: What is 'inheritance'? What is an example of inheritance?
# A 3: Inheritance is when another class object inherits properties and methods from it's parent.
class Motorcycle(Car):
    def __init__(self, make, modal, wheels, seats):
        Car.__init__(make, modal)
        self.wheels = 2
        self.seats = 1

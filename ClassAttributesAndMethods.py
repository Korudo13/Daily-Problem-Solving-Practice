# Make an example of a class attribute, and methods in a class in Python

class Dog(object):

    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed = 'Labrador')
geoffrey = Dog(breed = 'Huskie')

print sam.breed
print geoffrey.breed

print sam.species, geoffrey.species

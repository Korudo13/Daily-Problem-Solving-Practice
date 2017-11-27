# Create an example Class with a Class Object Attribute, and Methods within that Class in Python

class Dog(object):

    # Class Object Attribute
    species = 'mammal'

    # Initializing attributes 
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed = 'Labrador')
geoffrey = Dog(breed = 'Huskie')

print sam.breed
print geoffrey.breed

print sam.species, geoffrey.species

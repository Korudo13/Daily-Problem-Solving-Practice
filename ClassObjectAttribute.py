# Create an example Class with a Class Object Attribute, and Methods within that Class in Python

class Dog(object):

    # Class Object Attribute
    species = 'mammal'

    # Initializing Attributes
    def __init__(self, breed, name, temperment):
        self.breed = breed
        self.name = name
        self.temperment = temperment

dexter = Dog(breed = 'labrador', name = 'Dexter', temperment = 'silly')
balto = Dog(breed = 'huskie', name = 'Balto', temperment = 'chill')

print dexter.name, dexter.species, dexter.breed, dexter.temperment
print balto.name, balto.species, balto.breed, balto.temperment

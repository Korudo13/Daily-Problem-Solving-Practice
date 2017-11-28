# Use inheritance to create Derived Classes: Breakfast, Lunch, and Dinner from the Base Class: Meal

class Meal(object):

    def __init__(self):
        print 'This is a meal'

    def timeOfDay(self):
        print 'Any time of day'

        
class Breakfast(Meal):
    
    def __init__(self):
        Meal.__init__(self)
        print 'This is breakfast'

    def timeOfDay(self):
        print 'Morning'
        

class Lunch(Meal):

    def __init__(self):
        Meal.__init__(self)
        print 'This is lunch'

    def timeOfDay(self):
        print 'Afternoon'


        
class Dinner(Meal):
    def __init__(self):
        Meal.__init__(self)
        print 'This is dinner'

    def timeOfDay(self):
        print 'Evening'


b = Breakfast()
l = Lunch()
d = Dinner()

print b.timeOfDay()
print l.timeOfDay()
print d.timeOfDay()

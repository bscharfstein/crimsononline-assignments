"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""
building_spots = dict()

def findBuilding
    if (x,y) in building_spots
        return building_spots[(x,y)]
class Person:
    def __init__(self, name, surname, gender):
        self.name = name.title()
        if self.gender == "M":
            self.gender = gender
        elif self.gender == "F":
            self.gender = gender
        else: raise Exceptio("Gender must be M or F")
        self.name = name
        self.surname = surname
        self.gender = gender
        self.inside = False
        self.room_no = none

class Building(object):
    def __init__(self, (x,y)):
        self.rooms = dict()
        self.persons = []
        if (x,y) in building_spots:
            raise Exception("Lot already occupied")
        else:
            self.location = (x,y)

    def enter(self, person, room_no):
        if person.inside
            print("{} is already in the room)".format(person.name)
        else
            person.inside = True
            person.room_no = room_no
            self.persons += person

    def exit(self, person):
        person.inside = False
        person.room_no = None
        self.persons -= person

    def where_is(self, person):
        if person.inside == True
            print "{} is in room {}".format(person.name, self.room_no)
        else: print"{} is in room {}".format(person.name, person.room_no)

class Office(Building):
    def __init__(self, employees, (x,y)):
        super(Office, self).__init__((x,y))
        self.employees = employees

    def enter(self, person, room_no):
        if person.name in self.employees:
            super(Office, self).enter(person, room_no)
        else:
            print("{} is not an employee").format(person.name)

class House(building)
    def __init__(self):
        super(House, self).__init__():

    def enter(self, person):
        if person.inside == True
            print "Person already inside"
        else:
            self.persons += person

    def at_home(Person):
        return person.name in self.persons

    def where_is(self, person):
        print("not a valid function for Houses")


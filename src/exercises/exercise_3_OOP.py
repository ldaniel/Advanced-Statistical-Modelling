# Exercise 1 - Create an object called roc1 from the class below, passing 2 parameters, and then
# call attributes and methods.

from math import sqrt


class Rocket:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    def print_rocket(self):
        print(self.x, self.y)


roc1 = Rocket(1, 1)
roc1.move_rocket(2, 2)
roc1.print_rocket()


# Exercise 2 - Create a class called Person () with attributes: name, city, phone, and email. Use at least 2 special
# methods in your class. Create an object of your class and make a call to at least one of its special methods.

class Person:

    def __init__(self, name=None, city=None, phone=None, email=None):
        self.name = name
        self.city = city
        self.phone = phone
        self.email = email

    def __str__(self):
        return "%s lives in %s, phone number %s and email %s." % (self.name, self.city, self.phone, self.email)

    def call_phone(self):
        print("Calling number " + self.phone + "...")


mary = Person("Ana Maria", "São Paulo", "9988-7766", "maria@email.com")
mary.call_phone()
print(mary)


# Exercise 3 - Create the Smartphone class with 2 attributes, size and interface and create the MP3Player class with the
# attributes capacity. The MP3player class must inherit the attributes from the Smartphone class.

class Smartphone:

    def __init__(self, size=None, interface=None):
        self.size = size
        self.interface = interface


class MP3Player(Smartphone):
    def __init__(self, capacity=None):
        self.capacity = capacity
        Smartphone.__init__(self, size=None, interface=None)

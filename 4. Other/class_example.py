"""
This is an example for a car class. You are able to make multiple car objects and their properties will
be self contained in each individual object.

By convention, a class will always be named with the first letter capitalized.

The 'self' keyword is referring to that individual object. When you make the object, you don't have to pass anything
in for the 'self' parameter.
"""


class Car:

    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        self.on = False
        self.radio_on = False
        self.radio_station = 105.5

    def turn_on_radio(self):
        self.radio_on = True

    def turn_off_radio(self):
        self.radio_on = False

    def turn_car_on(self):
        self.on = True

    def turn_car_off(self):
        self.on = False

    def set_radio_station(self, station):
        self.radio_station = station

    def get_current_state(self):
        return self.on

    def get_current_station(self):
        return self.radio_station

    def get_car_model(self):
        return self.model

    def get_car_make(self):
        return self.make

    def get_car_color(self):
        return self.color


"""

Now this part will demonstrate how to use a class. 

"""


my_car = Car('White', 'Toyata', 'Camry')

print("My Car is currently: {}".format(my_car.get_current_state()))
my_car.turn_car_on()
print("My Car is currently: {}".format(my_car.get_current_state()))
my_car.set_radio_station(97.7)
print("My Car is currently playing radio station: {}".format(my_car.get_current_station()))

your_car = Car("Red", 'Chevrolet', 'Camaro')

print("My car is a {} {}. \nYour car is a {} {}".format(my_car.get_car_make(),
                                                         my_car.get_car_model(),
                                                         your_car.get_car_make(),
                                                         your_car.get_car_model()))
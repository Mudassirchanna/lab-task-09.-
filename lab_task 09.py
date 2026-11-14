# lab_ask 
"""Q:no:01 create a class named car.
.add attributes: brand and color.
.create a method start() that prints "the car is starting." """

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("The car is starting.")

car1 = Car("Audi", "Black")

print("Brand:", car1.brand)
print("Color:", car1.color)

car1.start()

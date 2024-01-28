class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self) -> None:
        # super().__init__()
        print("I am a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use is commute to work, and vacation with family")

class Motorcycle(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("I am a Motorcycle")
        # self.wheels = 2
        # self.has_roof = False

    def specific_usage(self):
        print("specific use is road trip, and racing")
        
c = Car()
c.general_usage()
c.specific_usage()
m = Motorcycle()
m.general_usage()
print(issubclass(Car,Motorcycle))
# Base class vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")  # Enforces implementation in subclasses


# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")


# Demonstrating polymorphism
def vehicle_action(vehicle):
    vehicle.move()


# Instantiate objects
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Create a list of vehicles
vehicles = [car, plane, boat, bicycle]

# Loop through and demonstrate polymorphism
for v in vehicles:
    vehicle_action(v)

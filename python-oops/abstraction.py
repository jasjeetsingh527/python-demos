# Abstract base class - defines the interface
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract vehicle class - hides implementation details"""

    @abstractmethod
    def start(self):
        """Abstract method - must be implemented by subclasses"""
        print("Main start")
        pass

    @abstractmethod
    def stop(self):
        """Abstract method - must be implemented by subclasses"""
        print("main stopß")
        pass


# Concrete implementations - each handles details differently
class Car(Vehicle):
    """Car implementation - specific details hidden from user"""

    def start(self):  # type: ignore
        # Complex engine starting logic hidden here
        return "Car engine started"

    def stop(self):  # type: ignore
        # Complex braking system logic hidden here
        return "Car stopped"


class Bicycle(Vehicle):
    """Bicycle implementation - different internal logic"""

    def start(self):  # type: ignore
        # Simple pedaling logic hidden here
        return "Started pedaling"

    def stop(self):  # type: ignore
        # Hand brake logic hidden here
        return "Applied brakes"


# Usage - user doesn't need to know internal details
def operate_vehicle(vehicle: Vehicle):
    """Function works with any vehicle - abstraction in action"""
    print(vehicle.start())  # Don't care HOW it starts
    print(vehicle.stop())  # Don't care HOW it stops


# Client code - simple interface, complex details hidden
if __name__ == "__main__":
    car = Car()
    bike = Bicycle()

    operate_vehicle(car)  # Works without knowing car internals
    operate_vehicle(bike)  # Works without knowing bike internals

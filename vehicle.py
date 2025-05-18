from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_specifications(self) -> str:
        pass


class Car(Vehicle):
    def drive(self):
        print("Driving a car...")

    def get_specifications(self):
        return "Car: 4 wheels, 5 seats, gasoline engine."


class Motorcycle(Vehicle):
    def drive(self):
        print("Riding a motorcycle...")

    def get_specifications(self):
        return "Motorcycle: 2 wheels, 2 seats, gasoline engine."


class Truck(Vehicle):
    def drive(self):
        print("Driving a truck...")

    def get_specifications(self):
        return "Truck: 6 wheels, 2 seats, diesel engine."
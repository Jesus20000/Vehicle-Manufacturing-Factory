from vehicle import Car, Motorcycle, Truck

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        vehicle_type = vehicle_type.lower()
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
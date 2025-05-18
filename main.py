from factory import VehicleFactory

def main():
    vehicle_type = input("Enter the type of vehicle you want to create (Car, Motorcycle, Truck): ")
    try:
        vehicle = VehicleFactory.create_vehicle(vehicle_type)
        vehicle.drive()
        print(vehicle.get_specifications())
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
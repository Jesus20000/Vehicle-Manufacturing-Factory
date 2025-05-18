Vehicle Factory - Factory Design Pattern

Overview:
This project demonstrates the Factory Design Pattern to create a flexible and centralized vehicle creation system. Vehicles such as Cars, Motorcycles, and Trucks implement a common interface and are created via a factory.

Files:
- vehicle.py: Abstract class Vehicle and concrete implementations (Car, Motorcycle, Truck).
- factory.py: VehicleFactory class with a static method to create vehicles.
- main.py: CLI interface for users to choose and create a vehicle.
- README.md: Project description and run instructions.

How to Run:
1. Make sure Python 3 is installed.
2. Save all files in the same folder.
3. Open terminal or command prompt and navigate to that folder.
4. Run the application with:

   python main.py

Expected Output:
The user is prompted to enter a vehicle type. The system creates the corresponding object and displays its drive behavior and specifications.

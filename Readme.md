# 🚗 Vehicle Manufacturing Factory

This project demonstrates the **Factory Design Pattern** in Python by simulating a vehicle manufacturing system. It enables the creation of different types of vehicles such as cars, motorcycles, and trucks from a centralized factory.

---

## 🛠️ Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- Factory Design Pattern

---

## 🧠 Design Pattern: Factory Method

The **Factory Pattern** provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. This is ideal for scalable systems like vehicle production where new product types can be added without altering the client code.

---

## 📁 Project Structure

- `vehicle.py` – Abstract base class `Vehicle` and concrete classes (`Car`, `Motorcycle`, `Truck`)  
- `factory.py` – `VehicleFactory` with a static method to create vehicles  
- `main.py` – Client script that interacts with the factory  
- `README.md` – Project documentation

---

## 🚀 Features

- Create vehicles like Car, Motorcycle, and Truck  
- Centralized object creation using a static factory method  
- Extendable to include more vehicle types  
- Clear separation between product definition and creation logic

---

## 📌 Sample Output

```

Enter the type of vehicle you want to create (Car, Motorcycle, Truck): car
Driving a car...
Car: 4 wheels, 5 seats, gasoline engine.

````

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/vehicle-manufacturing-factory.git
cd vehicle-manufacturing-factory
````

2. Run the main script:

```bash
python main.py
```

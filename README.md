
This project demonstrates clean and professional implementation of **Object-Oriented Programming (OOP)** concepts using Python.  
It includes:

✔️ Classes & Objects  
✔️ Encapsulation  
✔️ Inheritance  
✔️ **Method Overriding**  
✔️ **Using `super()`**  
✔️ Class Variables & Class Methods  
✔️ Object Management System  


## 📂 Project Structure

```text
Car_Management_System/
│── car_management.py     # Classes and logic
│── main.py               # Program execution
│── README.md             # Documentation
│── diagram.png           # UML Class Diagram
│── images/
       └── project_preview.png
```

## 🧠 OOP Concepts Implemented

| Concept        | Implemented? | Explanation                                   |
|---------------|--------------|-----------------------------------------------|
| Encapsulation | ✔️           | Using `__mileage` (private attribute)         |
| Inheritance   | ✔️           | `ElectricCar` inherits from `Car`            |
| Method Overriding | ✔️       | `ElectricCar.__str__()` overrides parent     |
| super() usage | ✔️           | Extends parent behavior in `__str__()`       |
| Class Variables | ✔️         | `total_cars`                                 |
| Class Methods | ✔️           | `show_total_cars()`                          |
| Polymorphism  | ✔️           | Printing objects uses overridden methods     |


## 📌 Files Summary

### `car_management.py`

- **Car Class**
  - Attributes: `brand`, `model`, `price`, `__mileage`
  - Methods: `get_mileage()`, `update_mileage()`, `show_total_cars()`, `__str__()`
- **ElectricCar Class**
  - Adds: `battery_capacity`
  - Overrides: `__str__()` using `super().__str__()`
  - Method: `info()` → returns same string as `__str__()`
- **CarManagement Class**
  - Manages a list of cars and prints them using polymorphism

### `main.py`

- Creates instances of `Car` and `ElectricCar`
- Adds them into `CarManagement`
- Displays total cars
- Shows all cars
- Updates mileage for one car
- Prints detailed info for the electric car

---

## ▶️ How to Run

1. Install **Python 3.x**
2. Download or clone this repository
3. Open a terminal / PowerShell in the project directory
4. Run:

```bash
python main.py
```

On Linux/macOS you may use:

```bash
python3 main.py
```

---

## 🧪 Sample Output

```text
Total cars: 3

All Cars:
Dodge Charger - $45000 - 15000 km
Ford Mustang - $30000 - 22000 km
Tesla Model S - $70000 - 100 kWh (Electric)

Update mileage for Dodge Charger:
Old mileage: 15000
New mileage: 20000

Electric car info:
Tesla Model S - $70000 - 100 kWh (Electric)
Direct print: Tesla Model S - $70000 - 100 kWh (Electric)
```

---

## 💡 What I Learned

- How to use **inheritance** to build advanced classes from a base class.  
- How to correctly implement **method overriding** in Python.  
- How to use `super()` to extend the behavior of parent methods.  
- How to apply **encapsulation** with private attributes.  
- How polymorphism works when printing different kinds of car objects.

---

## 🚀 Future Enhancements

- Add a third class: `HybridCar`  
- Save and load cars from a JSON or database file  
- Create a simple GUI using Tkinter  
- Add search and filter features in `CarManagement`  

---

## 6. Developers
This project was created by:

**Younis Oday Jalil**  
**Farah Khalid Yousef**

Cybersecurity Department  
University of Basrah  

---

## ✔️ License

Free to use for educational purposes.

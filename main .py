# main.py

from car_management import Car, CarManagement, ElectricCar

# إضافة سيارات عادية
car1 = Car("Dodge", "Charger", 45000, 15000)
car2 = Car("Ford", "Mustang", 30000, 22000)

# إضافة سيارة كهربائية
car3 = ElectricCar("Tesla", "Model S", 70000, 100, 5000)

# نخلي السيارات بالإدارة
CarManagement.add_car(car1)
CarManagement.add_car(car2)
CarManagement.add_car(car3)

# نطبع عدد السيارات
Car.show_total_cars()

# نعرض كل السيارات
print("\nAll Cars:")
CarManagement.show_all_cars()

# نجرّب تحديث الممشى
print("\nUpdate mileage for Dodge Charger:")
print("Old mileage:", car1.get_mileage())
car1.update_mileage(20000)
print("New mileage:", car1.get_mileage())

# نطبع معلومات السيارة الكهربائية
print("\nElectric car info:")
print(car3.info())      # info ترجع نفس نص __str__
print("Direct print of object:", car3)  # يبين شغل الـ __str__ أيضاً

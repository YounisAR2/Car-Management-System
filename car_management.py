# car_management.py

class Car:
    total_cars = 0     

    def __init__(self, brand, model, price, mileage=0):
        self.brand = brand          # عادي
        self.model = model          # عادي
        self.price = price          # عادي
        self.__mileage = mileage    # مخفي (Encapsulation)
        Car.total_cars += 1

    # Getter للممشى
    def get_mileage(self):
        return self.__mileage

    # تحديث الممشى (ما ينقص)
    def update_mileage(self, new_mileage):
        if new_mileage >= self.__mileage:
            self.__mileage = new_mileage
        else:
            print("Error: mileage cannot be decreased!")

    @classmethod
    def show_total_cars(cls):
        print("Total cars:", cls.total_cars)

    # ✅ دالة __str__ حتى تمثل الكائن كنص
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price} - {self.get_mileage()} km"


class ElectricCar(Car):
    def __init__(self, brand, model, price, battery_capacity, mileage=0):
        super().__init__(brand, model, price, mileage)
        self.battery_capacity = battery_capacity

    # ✅ Override + استخدام super().__str__()
    def __str__(self):
        base_info = super().__str__()     # يستدعي __str__ من Car
        return f"{base_info} - {self.battery_capacity} kWh (Electric)"

    # نستخدم info كواجهة إضافية)
    def info(self):
        # نرجع نفس النص مال __str__
        return str(self)


class CarManagement:
    cars_list = []   # Class Data

    @classmethod
    def add_car(cls, car_obj):
        cls.cars_list.append(car_obj)

    @classmethod
    def show_all_cars(cls):
        for car in cls.cars_list:
            # ✅ هسه نستخدم __str__ بدل بناء النص يدوي
            print(car)

# parent class
class Vehicle:
    def __init__(self, brand, model, year, plate_num, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.__plate_num = plate_num
        self.mileage = mileage
 
    def accelerate(self, speed):
        print(f"{self.year} {self.brand} {self.model} accelerated at {speed} km/h")
 
    def stop(self):
        print(f"{self.year} {self.brand} {self.model} has stopped")
 
    def steer(self, direction):
        print(f"{self.year} {self.brand} {self.model} is steering to the {direction}")
 
    def get_mileage(self):
        return self.mileage
 
    def get_plate_num(self):
        return self.__plate_num

# child class
class Car(Vehicle):
    def __init__(self, brand, model, year, plate_num, mileage, num_doors):
        super().__init__(brand, model, year, plate_num, mileage)
        self.num_doors = num_doors
 
    def lock_doors(self):
        print(f"{self.year} {self.brand} {self.model}: all {self.num_doors} doors locked")
 
    def get_num_doors(self):
        return self.num_doors

# aggregation
class Garage:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = []
 
    def add_car(self, car):
        self.cars.append(car)

# dependency
class Driver:
    def __init__(self, name):
        self.name = name
 
    def drive(self, car, direction):
        print(f"{self.name} is driving:")
        car.accelerate(60)
        car.steer(direction)
        car.stop()

# Test run:
print("--- TEST 1: INHERITANCE ---")
vehicle1 = Vehicle("Yamaha", "Mio", 2021, "DEF-1111", 3000)
car1 = Car("Toyota", "Vios", 2022, "ABC-6767", 67676, 4)
 
print(f"Parent object vehicle1: {vehicle1.brand} {vehicle1.model} {vehicle1.year} "
      f"{vehicle1.get_plate_num()} {vehicle1.get_mileage()}")
print(f"Child object car1 (inherited): {car1.brand} {car1.model} {car1.year} "
      f"{car1.get_plate_num()} {car1.get_mileage()}")
print(f"Child object car1 (own attribute): doors = {car1.get_num_doors()}")
car1.accelerate(80)
car1.lock_doors()
print(f"car1 is a Car:     {isinstance(car1, Car)}")
print(f"car1 is a Vehicle: {isinstance(car1, Vehicle)}")
 
print("\n--- TEST 2: AGGREGATION ---")
car2 = Car("Honda", "Civic", 2023, "XYZ-7777", 7777, 4)
garage1 = Garage("Car Garage", "Legazpi City")
garage1.add_car(car1)
garage1.add_car(car2)
 
print(f"Garage {garage1.name} ({garage1.location}) contains:")
for i, c in enumerate(garage1.cars, 1):
    print(f"  Car {i}: {c.brand} {c.model} {c.year} {c.get_plate_num()}")
 
del garage1
print(f"Garage deleted, but car1 still exists: {car1.brand} {car1.model}")
 
print("\n--- TEST 3: DEPENDENCY ---")
driver1 = Driver("Juan")
driver1.drive(car2, "left")
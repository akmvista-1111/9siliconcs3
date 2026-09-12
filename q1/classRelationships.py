class Car:
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


class Garage:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)


# --- BEFORE RELATIONSHIP ---
print("--- BEFORE RELATIONSHIP ---")

object1 = Car("Toyota", "Vios", 2022, "ABC-6767", 67676)
object2 = Car("Honda", "Civic", 2023, "XYZ-7777", 7777)
object3 = Car("Ford", "Ranger", 2021, "DEF-8888", 8888)

garage1 = Garage("Car Garage", "Legazpi City")

print("Objects have been created.")
print(f"Garage: {garage1.name}")
print(f"Object 1: {object1.brand} {object1.model}")
print(f"Object 2: {object2.brand} {object2.model}")
print(f"Object 3: {object3.brand} {object3.model}")


# --- BUILDING RELATIONSHIP ---
print("\n--- BUILDING RELATIONSHIP ---")

print("Adding cars to the garage.")

garage1.add_car(object1)
garage1.add_car(object2)
garage1.add_car(object3)


# --- AFTER RELATIONSHIP ---
print("\n--- AFTER RELATIONSHIP ---")

print(f"Garage: {garage1.name}")
print(f"Location: {garage1.location}")

print("Related objects:")

for car in garage1.cars:
    print(f"{car.brand} {car.model} {car.year} "
          f"{car.get_plate_num()} {car.get_mileage()}")
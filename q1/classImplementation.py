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


# --- BEFORE ---
print("Before:")

object1 = Car("Toyota", "Vios", 2022, "ABC-6767", 67676)
object2 = Car("Honda", "Civic", 2023, "XYZ-7777", 7777)

print(f"Object 1: {object1.brand} {object1.model} {object1.year} "
      f"{object1.get_plate_num()} {object1.get_mileage()}")

print(f"Object 2: {object2.brand} {object2.model} {object2.year} "
      f"{object2.get_plate_num()} {object2.get_mileage()}")

object1.accelerate(80)


# --- AFTER ---
print("\nAfter:")

print(f"Object 1: {object1.brand} {object1.model} {object1.year} "
      f"{object1.get_plate_num()} {object1.get_mileage()} 80")

print(f"Object 2: {object2.brand} {object2.model} {object2.year} "
      f"{object2.get_plate_num()} {object2.get_mileage()} 0")
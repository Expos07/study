class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine has started!")

    def show_info(self):
        print(f"{self.brand} {self.model} - Year: {self.year}, mileage: {self.mileage}")

    def drive(self):
        print(f"{self.brand} {self.model} is driving!")


car = Car("Toyota", "Corolla", 2020, 10)

car.drive()

car.show_info()
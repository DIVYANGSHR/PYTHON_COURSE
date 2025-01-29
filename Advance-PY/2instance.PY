class car:
    def __init__(self, make, model, year):
        self.make = make                     
        self.model = model
        self.year = year

    def start(self):                           
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def display_info(self):
        print(f"\nCar Information:\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n")


bmw = car(make="JEEP", model="SAUTH", year=2025)
unicorn = car(make="ERTIGA", model="INDIAN S", year=2026)

bmw.display_info()
bmw.start()
unicorn.display_info()
unicorn.start()
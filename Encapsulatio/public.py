class Car:
    def __init__(self, make, model, year):
        self.make = make                      
        self.model = model
        self.year = year

    def start(self):                           
        print(f"The {self.year} {self.make} {self.model} is starting.")
    

Innova = Car(make="Innova", model="Toyoto", year=2026)
Jeep =  Car (make="Jeep", model=  "Grand", year=2024)

Innova.start()
Jeep.start()

# print(Innova.model)
# print(Jeep.model)



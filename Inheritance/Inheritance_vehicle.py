class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand, self.model)

class Car(Vehicle):
    def mechanism(self):
        print("The vehicle is: ")

car_details = Car("TATA", "Safari")

car_details.mechanism()
car_details.display()
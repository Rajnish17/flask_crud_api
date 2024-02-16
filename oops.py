class Car:
    def __init__(self, name, price, model):
        self.name = name
        self.price = price
        self.model = model

    def __str__(self):
        return f"Car: {self.name}, Model: {self.model}, Price: {self.price}"

my_car = Car("Toyota", "555511", 2020)
print(my_car)

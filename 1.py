class Vehicle:
    def __init__(self, make, model):
        self.make=make
        self.model=model
    def get_info(self):
        return f"Марка: {self.make}, модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model,fuel_type):
        super().__init__(make, model)
        self.fuel_type=fuel_type

    def get_info(self):
        veh_info=super().get_info()
        return f"{veh_info}, тип топлива: {self.fuel_type}"


a=Vehicle("aser", "x3")
print(a.get_info())

b=Car("Nissan", "x3", "АИ95")
print(b.get_info())

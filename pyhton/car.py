class Car:
    def __init__(self, make, model, year, color, engine):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.color} {self.engine}"
    def engine2(self):
        return f"{self.year +3}"
    def name(self):
        return f"{self.make} {self.model} "

#object
car1 = Car("Ford", "Mustang", 2020, "Red", "Hemi_V8")
#object2
car2 = Car("mercedes","C63s", 2022, "Black", "Bi_turbo v8")
print(car1)
print(car1.engine2())
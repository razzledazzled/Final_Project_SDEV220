# Define your classes in this file

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

#Sample Dessert super class
class Dessert:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price


class Pie(Dessert):
    def __init__(self, flavor, price, filling_type, crust_type):
        super().__init__(flavor, price)
        self.filling_type = filling_type
        self.crust_type = crust_type


class Cake(Dessert):
    def __init__(self, flavor, price, frosting_type, layers):
        super().__init__(flavor, price)
        self.frosting_type = frosting_type
        self.layers = layers


class Cookie(Dessert):
    def __init__(self, flavor, price, size, texture):
        super().__init__(flavor, price)
        self.size = size
        self.texture = texture

class Dessert:
    def __init__(self, flavor, size, topping):
        self.flavor = flavor
        self.size = size
        self.topping = topping

    def __str__(self):
        return f"{self.size} {self.flavor} with {self.topping}"

class Pie(Dessert):
    def __init__(self, flavor, size, topping, filling):
        super().__init__(flavor, size, topping)
        self.filling = filling

    def __str__(self):
        return f"{self.size} {self.flavor} with {self.filling} filling, topped with {self.topping}"

class Cake(Dessert):
    def __init__(self, flavor, size, topping, layers):
        super().__init__(flavor, size, topping)
        self.layers = layers

    def __str__(self):
        return f"{self.size} {self.flavor} cake with {self.layers} layers, topped with {self.topping}"

class Cookie(Dessert):
    def __init__(self, flavor, size, topping, shape):
        super().__init__(flavor, size, topping)
        self.shape = shape

    def __str__(self):
        return f"{self.size} {self.flavor} cookie ({self.shape}), topped with {self.topping}"

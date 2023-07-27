class Dessert:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Pie:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.crust_type = None
        self.filling = None

    def set_crust_type(self, crust_type):
        crust_options = ["Regular", "Chocolate"]
        if crust_type in crust_options:
            self.crust_type = crust_type
        else:
            raise ValueError(f"Invalid crust type. Available options: {', '.join(crust_options)}")

    def set_filling(self, filling):
        filling_options = ["Cherry", "Apple", "Pumpkin"]
        if filling in filling_options:
            self.filling = filling
        else:
            raise ValueError(f"Invalid filling. Available options: {', '.join(filling_options)}")

    def calculate_price(self):
        # Add additional logic here to calculate the price based on the customization options
        pass

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}\nCrust: {self.crust_type}\nFilling: {self.filling}"



class Cake(Dessert):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"{super().__str__()}, Size: {self.size}"


class Cookies(Dessert):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def __str__(self):
        return f"{super().__str__()}, Quantity: {self.quantity}"

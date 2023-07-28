class Dessert:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Pie:
    def __init__(self):
        # Default values for a basic pie
        self.crust_type = "Regular"
        self.size = "Small"
        self.filling = "Apple"
        self.price = 10.00  # Base price for a basic pie

    def set_crust_type(self, crust_type):
        # Set the crust type and update the price accordingly
        if crust_type == "Regular":
            self.crust_type = "Regular"
            self.price += 0.00
        elif crust_type == "Graham Cracker":
            self.crust_type = "Graham Cracker"
            self.price += 2.00
        elif crust_type == "Chocolate":
            self.crust_type = "Chocolate"
            self.price += 3.00
        else:
            print("Invalid crust type.")

    def set_size(self, size):
        # Set the pie size and update the price accordingly
        if size == "Small":
            self.size = "Small"
            self.price += 0.00
        elif size == "Medium":
            self.size = "Medium"
            self.price += 5.00
        elif size == "Large":
            self.size = "Large"
            self.price += 10.00
        else:
            print("Invalid size.")

    def set_filling(self, filling):
        # Set the pie filling and update the price accordingly
        if filling == "Apple":
            self.filling = "Apple"
            self.price += 0.00
        elif filling == "Cherry":
            self.filling = "Cherry"
            self.price += 2.00
        elif filling == "Blueberry":
            self.filling = "Blueberry"
            self.price += 3.00
        else:
            print("Invalid filling.")

    def get_price(self):
        # Return the final price of the customized pie
        return self.price

class Cake():
    def __init__(self):
        # Default values for a basic cake
        self.flavor = "Vanilla"
        self.size = "Small"
        self.icing = "White Icing"
        self.toppings = "None"
        self.layers = 1
        self.price = 16.00  # Base price for a basic Cake

    def set_flavor(self, flavor):
    # Set the crust type and update the price accordingly
        if flavor == "Vanilla":
            self.flavor = "Regular"
            self.price += 0.00
        elif flavor == "Chocolate":
            self.flavor = "Chocolate"
            self.price += 2.00
        elif flavor == "Carrot":
            self.flavor = "Carrot"
            self.price += 3.00
        elif flavor == "New York Cheesecake":
            self.flavor = "New York Cheescake"
            self.price += 5.00
        else:
            print("Invalid crust type.")


class Cookies(Dessert):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def __str__(self):
        return f"{super().__str__()}, Quantity: {self.quantity}"

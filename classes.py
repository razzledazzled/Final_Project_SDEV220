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
            self.price += 8.00
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
        elif filling == "Pumpkin":
            self.filling = "Pumpkin"
            self.price += 3.50
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
        self.icing = "White"
        self.toppings = "No"
        self.layers = 1
        self.price = 16.00  # Base price for a basic Cake

    def set_flavor(self, flavor):
    # Set the flavor type and update the price accordingly
        if flavor == "Vanilla":
            self.flavor = "Vanilla"
            self.price += 0.00
        elif flavor == "Chocolate":
            self.flavor = "Chocolate"
            self.price += 1.50
        elif flavor == "Carrot":
            self.flavor = "Carrot"
            self.price += 2.00
        elif flavor == "New York Cheesecake":
            self.flavor = "New York Cheescake"
            self.price += 3.00
        else:
            print("Invalid flavor type.")

    def set_size(self, size):
        # Set the size and update the price accordingly
        if size == "Small":
            self.size = "Small"
            self.price += 5.00
        elif size == "Medium":
            self.size = "Medium"
            self.price += 7.0
        elif size == "Large":
            self.size = "Large"
            self.price += 11.0
        else:
            print("Invalid size type.")

    def set_icing(self, icing):
        # Set the icing and update the price accordingly
        if icing == "White Icing":
            self.icing = "White"
            self.price += 0.00
        elif icing == "Chocolate Icing":
            self.icing = "Chocolate"
            self.price += 0.5
        elif icing == "Berry Icing":
            self.icing = "Berry"
            self.price += 1.00
        else:
            print("Invalid icing type.")

    def set_toppings(self, toppings):
        # Set the icing and update the price accordingly
        if toppings == "None":
            self.toppings = "No"
            self.price += 0.00
        elif toppings == "Chocolate Shavings":
            self.toppings = "Chocolate Shavings"
            self.price += 0.1
        elif toppings == "Sprinkles":
            self.toppings = "Sprinkles for"
            self.price += 0.25
        elif toppings == "Coconut":
            self.toppings = "Coconut"
            self.price += 1.00
        else:
            print("Invalid topping type.")

    def set_layers(self, layers):
        # set the number of layers and price accordingly
        if layers == "1":
            self.layers = 1
            self.price += 0
        elif layers == "2":
            self.layers = 2
            self.price += 2.00
        elif layers == "3":
            self.layers = 3
            self.price += 4.00
        else:
            print("Invalid number of layers")

    def get_price(self):
        # Return the final price of the customized cake
        return self.price

class Cookie(Dessert):
    def __init__(self):
        # Default values for a basic cookie
        self.type = "Chewy"
        self.size = "Small"
        self.toppings = "No"
        self.quantity = 1
        self.price = 1.00  # Base price for a basic cookie

    def set_quantity(self, quantity):
        # Set the quantity and update the price accordingly
        if quantity == "Single":
            self.quantity = 1
            self.price += 0.00
        elif quantity == "Double":
            self.quantity = 2
            self.price += 1.00
        elif quantity == "6 Pack":
            self.quantity = 6
            self.price += 5.50
        elif quantity == "Dozen":
            self.quantity = 12
            self.price += 10.15
        elif quantity == "Baker's Dozen":
            self.quantity = 13
            self.price += 11.25
        else:
            print("Invalid quantity.")

    def set_type(self, type):
        # Set the type of cookie and update the price accordingly
        if type == "Chewy":
            self.type = "Chewy"
            self.price += 0.00
        elif type == "Crunchy":
            self.type = "Crunchy"
            self.price += 0.00
        elif type == "Sugar":
            self.type = "Sugar"
            self.price += 0.25
        elif type == "Sandwich":
            self.type = "Sandwich"
            self.price += 1.00
        else:
            print("Invalid type.")

    def set_size(self, size):
        # Set the size of cookie and update the price accordingly
        if size == "Small":
            self.size = "Small"
            self.price += 0.00
        elif size == "Medium":
            self.size = "Medium"
            self.price += 0.00
        elif size == "Large":
            self.size = "Large"
            self.price += 0.25
        elif size == "Royal":
            self.size = "Royal"
            self.price += 1.00
        else:
            print("Invalid size.")

    def set_topping(self, topping):
        # Set the topping of the cookie and update the price accordingly
        if topping == "None":
            self.topping = "No"
            self.price += 0.00
        elif topping == "Chocolate Chip":
            self.topping = "Chocolate Chip"
            self.price += 0.00
        elif topping == "Frosting":
            self.topping = "Frosting"
            self.price += 0.25
        elif topping == "Macadamia Nut":
            self.topping = "Macadmia Nut"
            self.price += .50
        elif topping == "Ice Cream":
            self.topping = "Ice Cream"
            self.price += 2.00
        else:
            print("Invalid topping.")

    def get_price(self):
        # Return the final price of the customized cookie
        return self.price

    def __str__(self):
        return f"{super().__str__()}, Quantity: {self.quantity}"

# Define your classes in this file

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

class Cake(Desserts):
    def __init__(self, cake_flavor, cake_icing, cake_topping, price):
        super().__init__(cake_flavor, price)
        self.cake_flavor = cake_flavor
        self.cake_icing = cake_icing
        self.cake_topping = cake_topping
        self. price = price 
        
# cake options entered
cake_flavor_s=input("Cake Flavor: ")
cake_icing_s=input("Icing Flavor: ")
cake_topping_s=input("Cake Topping: ")
price_s=input("Enter Total Price: ")
pastry=Cake(cake_flavor_s,cake_icing_s, cake_topping_s, price_s) 

# print final product details
print("\nFlavor: "+pastry.cake_flavor)
print("\nIcing: "+pastry.cake_icing)
print("\nToppings: "+pastry.cake_topping)
print("\nPrice: "+pastry.price)

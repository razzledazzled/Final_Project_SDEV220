# Define your classes in this file

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")
class Pie(Dessert):
    def __init__(self, flavor, price, filling_type, crust_type):
        super().__init__(flavor, price)
        self.filling_type = filling_type
        self.crust_type = crust_type
        self.flavor = flavor
        self. price = price 
# customers can enter what they want
flavor_s=input("Type of flavor :")
price_s=input("Enter a price :")
filling_type_s=input("Type of flavor :")
crust_type_s=input("Type of crust :")
pastry=Pie(flavor_s,price_s,filling_type_s,crust_type_s) 
# then print the details
print("\nflavor :"+pastry.flavor)
print("\nprice :"+pastry.price)
print("\nfilling :"+pastry.filling_type)
print("\nCrust Type :"+pastry.crust_type)

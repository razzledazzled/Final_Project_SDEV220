import tkinter as tk
from tkinter import messagebox
from classes import Pie
from classes import Cake
from classes import Cookie

class DessertOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pie or Die: Customize Your Order")
        
        self.cart = []  # List to store the selected desserts
        
        self.create_widgets()

    def create_widgets(self):
        # Create the buttons for each dessert type
        pie_button = tk.Button(self.root, text="Build Your Pie", command=self.open_pie_customization)
        pie_button.pack()

        cake_button = tk.Button(self.root, text="Customize Your Cake", command=self.open_cake_customization)
        cake_button.pack()

        cookie_button = tk.Button(self.root, text="Create Your Cookies", command=self.open_cookie_customization)
        cookie_button.pack()

        # Create a cart button to view the cart
        cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        cart_button.pack(side='right', anchor='ne', padx=10, pady=10)

    def open_pie_customization(self):
        # Create a new subwindow for customizing the pie
        pie_customization_window = tk.Toplevel(self.root)
        pie_customization_window.title("Customize Pie")

        # Set the width and height of the window
        pie_customization_window.geometry("600x500")

        # Create a new instance of the Pie class for customization
        pie_instance = Pie()

        # Create a variable to store the selected options
        crust_var = tk.StringVar()
        size_var = tk.StringVar()
        filling_var = tk.StringVar()

        # Function to add the customized pie to the cart
        def add_to_cart():
            pie_instance.set_crust_type(crust_var.get())
            pie_instance.set_size(size_var.get())
            pie_instance.set_filling(filling_var.get())
            self.cart.append(pie_instance)
            messagebox.showinfo("Success", "Pie added to cart!")
            # Close the "Customize Pie" subwindow after adding to the cart
            pie_customization_window.destroy()

        # Create option menus for each pie attribute
        crust_label = tk.Label(pie_customization_window, text="Crust Type:")
        crust_label.pack()
        crust_menu = tk.OptionMenu(pie_customization_window, crust_var, "Regular", "Graham Cracker", "Chocolate")
        crust_menu.pack()

        size_label = tk.Label(pie_customization_window, text="Size:")
        size_label.pack()
        size_menu = tk.OptionMenu(pie_customization_window, size_var, "Small", "Medium", "Large")
        size_menu.pack()

        filling_label = tk.Label(pie_customization_window, text="Filling:")
        filling_label.pack()
        filling_menu = tk.OptionMenu(pie_customization_window, filling_var, "Apple", "Cherry", "Blueberry", "Pumpkin")
        filling_menu.pack()

        # Button to add the customized pie to the cart
        add_to_cart_button = tk.Button(pie_customization_window, text="Add to Cart", command=add_to_cart)
        add_to_cart_button.pack()

    def open_cake_customization(self):
        # Create a new subwindow for customizing the cake
        cake_customization_window = tk.Toplevel(self.root)
        cake_customization_window.title("Customize Cake")

        # Set the width and height of window
        cake_customization_window.geometry("600x500")

        # Create a new instance of the Cake class for customization
        cake_instance = Cake()

        # Create a variable to store the selected options
        flavor_var = tk.StringVar()
        size_var = tk.StringVar()
        icing_var = tk.StringVar()
        toppings_var = tk.StringVar()
        layers_var = tk.StringVar()

        # Function to add the cusomized cake to the chart
        def add_to_cart():
            cake_instance.set_flavor(flavor_var.get())
            cake_instance.set_size(size_var.get())
            cake_instance.set_icing(icing_var.get())
            cake_instance.set_toppings(toppings_var.get())
            self.cart.append(cake_instance)
            messagebox.showinfo("Success", "Cake added to cart!")
            # Close the "Customize Cake" subwindow after adding to the cart
            cake_customization_window.destroy()
        
        #Create option menus for each cake attribute
        flavor_label = tk.Label(cake_customization_window, text="Flavor Type:")
        flavor_label.pack()
        flavor_menu = tk.OptionMenu(cake_customization_window, flavor_var, "Vanilla", "Chocolate", "Carrot", "New York Cheesecake")
        flavor_menu.pack()
        size_label = tk.Label(cake_customization_window, text="Size:")
        size_label.pack()
        size_menu = tk.OptionMenu(cake_customization_window, size_var, "Small", "Medium", "Large")
        size_menu.pack()
        icing_label = tk.Label(cake_customization_window, text="Icing Type:")
        icing_label.pack()
        icing_menu = tk.OptionMenu(cake_customization_window, icing_var, "White Icing", "Chocolate Icing", "Berry Icing")
        icing_menu.pack()
        toppings_label = tk.Label(cake_customization_window, text="Topping:")
        toppings_label.pack()
        toppings_menu = tk.OptionMenu(cake_customization_window, toppings_var, "None", "Chocolate Shavings", "Sprinkles", "Coconut")
        toppings_menu.pack()
        
        # Button to add the customized pie to the cart
        add_to_cart_button = tk.Button(cake_customization_window, text="Add to Cart", command=add_to_cart)
        add_to_cart_button.pack()

    def open_cookie_customization(self):
        # Create a new subwindow for customizing the cookie
        cookie_customization_window = tk.Toplevel(self.root)
        cookie_customization_window.title("Customize Cookie")

        # Set the width and height of window
        cookie_customization_window.geometry("600x500")

    def view_cart(self):
        # Display the selected desserts in the cart
        if not self.cart:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")
        else:
            cart_items = []
            for dessert in self.cart:
                if isinstance(dessert, Pie):
                    cart_items.append(f"{dessert.size} {dessert.filling} pie ({dessert.crust_type} crust): ${dessert.get_price():.2f}")
                elif isinstance(dessert, Cake):
                    cart_items.append(f"{dessert.size} {dessert.flavor} cake with {dessert.icing} icing and {dessert.toppings} toppings ({dessert.layers} layers): ${dessert.get_price():.2f}")
                elif isinstance(dessert, Cookie):
                    cart_items.append(f"{dessert.quantity} {dessert.size} {dessert.type} cookies with {dessert.toppings}: ${dessert.get_price():.2f}")


        cart_text = "\n".join(cart_items)
        messagebox.showinfo("Cart", f"Cart items:\n{cart_text}")



if __name__ == "__main__":
    root = tk.Tk()
    app = DessertOrderApp(root)

    # Set the width and height of the main window
    root.geometry("400x300")

    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from classes import Pie

# Import the Pie class from the previous code snippet
# Make sure the Pie class is defined in the same script or imported properly

class DessertOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dessert Order App")
        
        self.cart = []  # List to store the selected desserts
        
        self.create_widgets()

    def create_widgets(self):
        # Create the buttons for each dessert type
        pie_button = tk.Button(self.root, text="Pie", command=self.open_pie_customization)
        pie_button.pack()

        # Create a cart button to view the cart
        cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        cart_button.pack()

    def open_pie_customization(self):
        # Create a new subwindow for customizing the pie
        pie_customization_window = tk.Toplevel(self.root)
        pie_customization_window.title("Customize Pie")

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
        filling_menu = tk.OptionMenu(pie_customization_window, filling_var, "Apple", "Cherry", "Blueberry")
        filling_menu.pack()

        # Button to add the customized pie to the cart
        add_to_cart_button = tk.Button(pie_customization_window, text="Add to Cart", command=add_to_cart)
        add_to_cart_button.pack()

    def view_cart(self):
        # Display the selected desserts in the cart
        if not self.cart:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")
        else:
            cart_items = "\n".join([f"{dessert.crust_type} Pie ({dessert.size}, {dessert.filling}): ${dessert.get_price():.2f}" for dessert in self.cart])
            messagebox.showinfo("Cart", f"Cart items:\n{cart_items}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DessertOrderApp(root)
    root.mainloop()

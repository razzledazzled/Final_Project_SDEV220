import tkinter as tk
from tkinter import ttk
from classes import Pie, Cake, Cookie

def order_desserts():
    # Get the quantities of each dessert
    pie_qty = pie_spinbox.get()
    cake_qty = cake_spinbox.get()
    cookie_qty = cookie_spinbox.get()

    # Create dessert objects with the given quantities
    pie = Pie(flavor="Apple", size="Medium", topping="Ice cream", filling="Apple")
    cake = Cake(flavor="Chocolate", size="Large", topping="Sprinkles", layers=2)
    cookie = Cookie(flavor="Chocolate Chip", size="Small", topping="Chocolate drizzle", shape="Circle")

    # For now, let's just print the order summary
    print("Order Summary:")
    print(f"Pies: {pie_qty}, {pie}")
    print(f"Cakes: {cake_qty}, {cake}")
    print(f"Cookies: {cookie_qty}, {cookie}")

def customize_desserts():
    # Create widgets for the customization page
    customize_frame = ttk.Frame(tab2)
    customize_frame.pack(fill="both", expand=True)

    # Add widgets for customizing desserts (you can modify this part based on your desired options)
    label = ttk.Label(customize_frame, text="Customize your desserts:")
    label.pack()

    # For example, you can use Entry widgets, Checkbuttons, Radiobuttons, etc., for different attributes.
    # Here, we use simple Entry widgets to allow the user to specify custom flavors for each dessert.
    pie_flavor_label = ttk.Label(customize_frame, text="Pie Flavor:")
    pie_flavor_label.pack()
    pie_flavor_entry = ttk.Entry(customize_frame)
    pie_flavor_entry.pack()

    cake_flavor_label = ttk.Label(customize_frame, text="Cake Flavor:")
    cake_flavor_label.pack()
    cake_flavor_entry = ttk.Entry(customize_frame)
    cake_flavor_entry.pack()

    cookie_flavor_label = ttk.Label(customize_frame, text="Cookie Flavor:")
    cookie_flavor_label.pack()
    cookie_flavor_entry = ttk.Entry(customize_frame)
    cookie_flavor_entry.pack()

    # Add a "Confirm" button to save the customization
    confirm_button = ttk.Button(customize_frame, text="Confirm", command=save_customization)
    confirm_button.pack()

def save_customization():
    # Retrieve the selected custom flavors for each dessert
    pie_flavor = pie_flavor_entry.get()
    cake_flavor = cake_flavor_entry.get()
    cookie_flavor = cookie_flavor_entry.get()

    # Use the selected custom flavors to update the dessert objects accordingly
    Pie.flavor = pie_flavor
    Cake.flavor = cake_flavor
    Cookie.flavor = cookie_flavor

    # Print a confirmation message
    print("Customization saved!")

# Create the main application window
root = tk.Tk()
root.title("Dessert Customization")

# Create a notebook to handle multiple tabs/pages
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Tab 1 - Order Page
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Order")

label = ttk.Label(tab1, text="How many of each dessert would you like to order?")
label.pack()

# Pie
pie_label = ttk.Label(tab1, text="Pies:")
pie_label.pack()
pie_spinbox = ttk.Spinbox(tab1, from_=0, to=10)
pie_spinbox.pack()

# Cake
cake_label = ttk.Label(tab1, text="Cakes:")
cake_label.pack()
cake_spinbox = ttk.Spinbox(tab1, from_=0, to=10)
cake_spinbox.pack()

# Cookie
cookie_label = ttk.Label(tab1, text="Cookies:")
cookie_label.pack()
cookie_spinbox = ttk.Spinbox(tab1, from_=0, to=10)
cookie_spinbox.pack()

# Order button
order_button = ttk.Button(tab1, text="Next", command=customize_desserts)
order_button.pack()

# Tab 2 - Customization Page (will be created when "Next" button is clicked)
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Customize")

# Start the main event loop
root.mainloop()

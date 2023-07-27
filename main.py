import tkinter as tk
from tkinter import ttk

from classes import Pie

def customize_dessert(dessert_name):
    if dessert_name == "Pie":
        pie_customization_window = tk.Toplevel(root)
        pie_customization_window.title("Customize your Pie!")

        # Create a new instance of Pie
        pie = Pie("Custom Pie", price=0.00)

        # Function to update the selected crust type
        def set_crust_type(*args):
            crust_type = crust_var.get()
            pie.set_crust_type(crust_type)

        # Function to update the selected filling
        def set_filling(*args):
            filling = filling_var.get()
            pie.set_filling(filling)

        # Label and option menu for crust type
        crust_label = tk.Label(pie_customization_window, text="Crust Type:")
        crust_label.pack(padx=10, pady=5)

        crust_options = ["Regular", "Chocolate"]
        crust_var = tk.StringVar(pie_customization_window)
        crust_var.set(crust_options[0])  # Set the default value
        crust_var.trace("w", set_crust_type)  # Call set_crust_type when the value changes

        crust_option_menu = ttk.OptionMenu(pie_customization_window, crust_var, *crust_options)
        crust_option_menu.pack(padx=10, pady=5)

        # Label and option menu for filling
        filling_label = tk.Label(pie_customization_window, text="Filling:")
        filling_label.pack(padx=10, pady=5)

        filling_options = ["Cherry", "Apple", "Pumpkin"]
        filling_var = tk.StringVar(pie_customization_window)
        filling_var.set(filling_options[0])  # Set the default value
        filling_var.trace("w", set_filling)  # Call set_filling when the value changes

        filling_option_menu = ttk.OptionMenu(pie_customization_window, filling_var, *filling_options)
        filling_option_menu.pack(padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dessert Ordering System")

    # Sample dessert names
    desserts = ["Pie", "Cake", "Cookies"]

    # Create a frame to hold the dessert names and buttons
    dessert_frame = tk.Frame(root, padx=20, pady=20)
    dessert_frame.pack()

    # Display the dessert names and "Customize" buttons side by side using the grid layout
    for index, dessert in enumerate(desserts):
        dessert_label = tk.Label(dessert_frame, text=dessert, font=("Arial", 14))
        dessert_label.grid(row=index, column=0, padx=10, pady=10)

        customize_button = tk.Button(dessert_frame, text="Customize", command=lambda dessert_name=dessert: customize_dessert(dessert_name))
        customize_button.grid(row=index, column=1, padx=10, pady=10)

    root.mainloop()

from tkinter import Tk, Label, Button, Entry, StringVar, IntVar
from classes import Pie, Cake, Cookie

class DessertApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dessert Customizer")

        self.dessert_quantities = {
            "Pie": IntVar(),
            "Cake": IntVar(),
            "Cookie": IntVar()
        }

        self.customizations = []

        self.create_quantity_page()

    def create_quantity_page(self):
        Label(self.root, text="Choose the quantity of each dessert:").pack()

        for dessert_type, var in self.dessert_quantities.items():
            Label(self.root, text=dessert_type).pack()
            Entry(self.root, textvariable=var).pack()

        Button(self.root, text="Next", command=self.create_customization_page).pack()

    def create_customization_page(self):
        Label(self.root, text="Customize your desserts:").pack()

        for dessert_type, quantity_var in self.dessert_quantities.items():
            quantity = quantity_var.get()
            if quantity > 0:
                Label(self.root, text=dessert_type).pack()
                for _ in range(quantity):
                    dessert_customization = {}

                    Label(self.root, text="Flavor:").pack()
                    flavor_entry = Entry(self.root)
                    flavor_entry.pack()
                    dessert_customization["flavor"] = flavor_entry

                    if dessert_type == "Pie":
                        Label(self.root, text="Filling:").pack()
                        filling_entry = Entry(self.root)
                        filling_entry.pack()
                        dessert_customization["filling"] = filling_entry

                        Label(self.root, text="Crust:").pack()
                        crust_entry = Entry(self.root)
                        crust_entry.pack()
                        dessert_customization["crust"] = crust_entry

                    elif dessert_type == "Cake":
                        Label(self.root, text="Frosting:").pack()
                        frosting_entry = Entry(self.root)
                        frosting_entry.pack()
                        dessert_customization["frosting"] = frosting_entry

                        Label(self.root, text="Layers:").pack()
                        layers_entry = Entry(self.root)
                        layers_entry.pack()
                        dessert_customization["layers"] = layers_entry

                    elif dessert_type == "Cookie":
                        Label(self.root, text="Size:").pack()
                        size_entry = Entry(self.root)
                        size_entry.pack()
                        dessert_customization["size"] = size_entry

                        Label(self.root, text="Texture:").pack()
                        texture_entry = Entry(self.root)
                        texture_entry.pack()
                        dessert_customization["texture"] = texture_entry

                    self.customizations.append(dessert_customization)

        Button(self.root, text="Submit", command=self.display_customization).pack()

    def display_customization(self):
        Label(self.root, text="Your Dessert Customization:").pack()

        for dessert_customization in self.customizations:
            flavor_entry = dessert_customization["flavor"]
            dessert_type = None
            dessert = None

            for dessert_type in self.dessert_quantities:
                if flavor_entry.get():
                    if dessert_type == "Pie":
                        filling_entry = dessert_customization["filling"]
                        crust_entry = dessert_customization["crust"]
                        dessert = Pie(
                            flavor_entry.get(),
                            filling_entry.get(),
                            crust_entry.get()
                        )
                    elif dessert_type == "Cake":
                        frosting_entry = dessert_customization["frosting"]
                        layers_entry = dessert_customization["layers"]
                        dessert = Cake(
                            flavor_entry.get(),
                            frosting_entry.get(),
                            layers_entry.get()
                        )
                    elif dessert_type == "Cookie":
                        size_entry = dessert_customization["size"]
                        texture_entry = dessert_customization["texture"]
                        dessert = Cookie(
                            flavor_entry.get(),
                            size_entry.get(),
                            texture_entry.get()
                        )
                    break

            if dessert:
                Label(self.root, text=f"Dessert Type: {dessert_type}").pack()
                Label(self.root, text=f"Flavor: {dessert.flavor}").pack()

                if isinstance(dessert, Pie):
                    Label(self.root, text=f"Filling: {dessert.filling}").pack()
                    Label(self.root, text=f"Crust: {dessert.crust}").pack()

                elif isinstance(dessert, Cake):
                    Label(self.root, text=f"Frosting: {dessert.frosting}").pack()
                    Label(self.root, text=f"Layers: {dessert.layers}").pack()

                elif isinstance(dessert, Cookie):
                    Label(self.root, text=f"Size: {dessert.size}").pack()
                    Label(self.root, text=f"Texture: {dessert.texture}").pack()

root = Tk()
DessertApp(root)
root.mainloop()

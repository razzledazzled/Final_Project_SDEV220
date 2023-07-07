from tkinter import Tk, Label, Button, Entry
from tkinter import StringVar, IntVar
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

        self.flavor_entries = []
        self.topping_entries = []

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
                for i in range(quantity):
                    Label(self.root, text=f"Dessert {i+1}:").pack()
                    flavor_entry = Entry(self.root)
                    flavor_entry.pack()
                    self.flavor_entries.append(flavor_entry)

                    if dessert_type == "Pie":
                        filling_entry = Entry(self.root)
                        filling_entry.pack()
                        self.topping_entries.append(filling_entry)

                        crust_entry = Entry(self.root)
                        crust_entry.pack()
                        self.topping_entries.append(crust_entry)

                    elif dessert_type == "Cake":
                        frosting_entry = Entry(self.root)
                        frosting_entry.pack()
                        self.topping_entries.append(frosting_entry)

                        layers_entry = Entry(self.root)
                        layers_entry.pack()
                        self.topping_entries.append(layers_entry)

                    elif dessert_type == "Cookie":
                        size_entry = Entry(self.root)
                        size_entry.pack()
                        self.topping_entries.append(size_entry)

                        texture_entry = Entry(self.root)
                        texture_entry.pack()
                        self.topping_entries.append(texture_entry)

        Button(self.root, text="Submit", command=self.submit_customization).pack()

    def submit_customization(self):
        desserts = []

        for i, dessert_type in enumerate(self.dessert_quantities):
            quantity = self.dessert_quantities[dessert_type].get()
            for j in range(quantity):
                flavor = self.flavor_entries[i * quantity + j].get()

                if dessert_type == "Pie":
                    filling = self.topping_entries[i * 2 + j * 2].get()
                    crust = self.topping_entries[i * 2 + j * 2 + 1].get()
                    dessert = Pie(flavor, 0, filling, crust)

                elif dessert_type == "Cake":
                    frosting = self.topping_entries[i * 2 + j * 2].get()
                    layers = self.topping_entries[i * 2 + j * 2 + 1].get()
                    dessert = Cake(flavor, 0, frosting, layers)

                elif dessert_type == "Cookie":
                    size = self.topping_entries[i * 2 + j * 2].get()
                    texture = self.topping_entries[i * 2 + j * 2 + 1].get()
                    dessert = Cookie(flavor, 0, size, texture)

                desserts.append(dessert)

        self.display_customization(desserts)

    def display_customization(self, desserts):
        Label(self.root, text="Your Dessert Customization:").pack()

        for dessert in desserts:
            Label(self.root, text=f"Flavor: {dessert.flavor}").pack()

            if isinstance(dessert, Pie):
                Label(self.root, text=f"Filling: {dessert.filling_type}").pack()
                Label(self.root, text=f"Crust: {dessert.crust_type}").pack()

            elif isinstance(dessert, Cake):
                Label(self.root, text=f"Frosting: {dessert.frosting_type}").pack()
                Label(self.root, text=f"Texture: {dessert.texture}").pack()


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

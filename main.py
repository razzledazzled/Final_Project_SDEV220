# Import the necessary classes and modules
from tkinter import Tk, Button
from classes import MyClass

# Create an instance of the class
my_object = MyClass("John")

# Define a function to execute on button click
def button_click():
    my_object.greet()

# Create the GUI window
window = Tk()

# Create a button that calls the function on click
button = Button(window, text="Click Me!", command=button_click)
button.pack()

# Start the Tkinter event loop
window.mainloop()

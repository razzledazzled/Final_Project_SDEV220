import tkinter as tk

# Create a new instance of Tkinter window
window = tk.Tk()

# Set the window title
window.title("My GUI Application")

# Create a label widget
label = tk.Label(window, text="Hello, World!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me!")
button.pack()

# Function to execute when the button is clicked
def button_click():
    label.config(text="Button Clicked!")

# Bind the button click event to the function
button.config(command=button_click)

# Start the Tkinter event loop
window.mainloop()

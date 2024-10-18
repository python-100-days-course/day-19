# Referances:
# https://stackoverflow.com/questions/56960444/how-to-make-text-into-a-button-in-python-turtle
# https://www.w3resource.com/python-exercises/tkinter/python-tkinter-custom-widgets-and-themes-exercise-1.php

import turtle
import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.FLAT,  # Remove button relief
            bd=1,  # Thin border
            highlightthickness=0,  # Remove highlight
            padx=0,  # Add horizontal padding
            pady=0,  # Add vertical padding
            height=10,
            width=10,
            font=("Arial", 12),  # Set font
            foreground="white",  # Text color
            background="black",  # Background color
            activeforeground="white", # Hover text color
            activebackground="black", # Hover background color
        )
    #     # Bind events
    #     self.bind("<Enter>", self.on_hover)
    #     self.bind("<Leave>", self.on_leave)
    #
    # def on_hover(self, event):
    #     self.config(background="black")  # Change color on hover
    #
    # def on_leave(self, event):
    #     self.config(background="black")  # Restore original color

# # Create the main window
# root = tk.Tk()
# root.title("Custom Button Example")
#
# # Create a custom button
# custom_button = CustomButton(root, text="Custom Button")
# custom_button.pack(pady=20)

def show_cat():
    turtle.ht()
    turtle.penup()
    turtle.goto (15, 220)
    turtle.color("black")
    turtle.write("CAT", move=False, align="center", font=("Times New Roman", 120, "bold"))

screen = turtle.Screen()
screen.setup(800,800)

canvas = screen.getcanvas()

button = CustomButton(canvas.master, text="Click Me", command=show_cat)
canvas.create_window(0, 0, window=button)

#canvas.create_rectangle((100, 100, 700, 300))

turtle.mainloop()
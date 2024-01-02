import tkinter as tk
import ttkbootstrap as tb

root = tb.Window(themename="morph")

root.title("Grid Example")

# Creating widgets
heading = tb.Label(root, text="This is a Form", font=('Impact', 14, 'bold'))
grid_frame = tb.Frame(root)
label1 = tb.Label(grid_frame, text="Label 1")
label2 = tb.Label(grid_frame, text="Label 2")
entry1 = tb.Entry(grid_frame)
entry2 = tb.Entry(grid_frame)
button = tb.Button(grid_frame, text="Submit")

# Using grid to place widgets
heading.pack()
grid_frame.pack()
label1.grid(row=0, column=0, padx=10, pady=5)
label2.grid(row=1, column=0, padx=10, pady=5)
entry1.grid(row=0, column=1, columnspan=2, padx=10, pady=5)
entry2.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()

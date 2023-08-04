from tkinter import *


def button_click():
    miles = int(user_input.get())
    calculated_kilometres = round(miles * 1.689)
    calculated_label.config(text=calculated_kilometres)


window = Tk()
window.title("Miles to Kilometres Converter")

user_input = Entry(width=7)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

calculated_label = Label(text="0")
calculated_label.grid(column=1, row=1)

kilometres_label = Label(text="Km")
kilometres_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_click)
calculate_button.grid(column=1, row=2)


window.mainloop()
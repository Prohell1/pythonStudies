from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from string import ascii_letters, digits, punctuation
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ascii_letters
    numbers = digits
    symbols = punctuation

    rnd_letters = [choice(letters) for _ in range(randint(8, 10))]
    rnd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    rnd_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = rnd_letters + rnd_symbols + rnd_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- Find Password ------------------------------- #


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        website = website_entry.get()
        email = data[website]["email"]
        password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No details for website: '{website}' exists.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    is_input_valid = len(website) > 0 and len(email) > 0 and len(password) > 0

    if is_input_valid:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "prohell@outlook.hu")

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import os.path
from random import choice, randint, shuffle
import pyperclip

window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    path = './saved_password.txt'
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 and len(password) > 0:
        is_okay = messagebox.askokcancel(title=website, message=f"You have entered the following details: \n"
                                                                f"Email: {email} \nPassword: {password} "
                                                                f"\nIs it okay to save? ")
        if is_okay:
            if os.path.isfile(path):
                method = "a"
            else:
                method = "w"
            with open(path, method) as password_file:
                password_file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "prince.agyei.tuffour@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)


# Buttons
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

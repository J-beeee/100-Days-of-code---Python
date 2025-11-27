import json
from tkinter import *
from tkinter import messagebox
from random import randint, sample
import pyperclip
# ---------------------------- GLOBALS ------------------------------- #
FONT = ("Comic Sans MS", 14 , "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0,END)
    password_output = ""
    categories = {
        'lc': (97, 122, randint(6,8)),
        'uc': (65, 90, randint(1,3)),
        'num': (48, 57, randint(1,3)),
        'sc': (33, 47, randint(1,3))
    }
    for low, high, count in categories.values():
        for _ in range(count):
            password_output += chr(randint(low, high))
    password_output = "".join(sample(password_output,len(password_output)))
    password_input.insert(0, password_output)
    pyperclip.copy(password_output)
# ---------------------------- SEARCH DATA ------------------------------- #
def search_data(website):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    try:
        messagebox.showinfo(title=website, message=f"Email: {data[website]["username"]}\nPassword: {data[website]["password"]}")
    except KeyError as Errormessage:
        messagebox.showinfo(title=f"{Errormessage}", message="An Error occurred.")
    except FileNotFoundError as Errormessage:
        messagebox.showinfo(title=f"{Errormessage}", message="An Error occurred.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(website, mail, password):
    new_data = {
        website: {
            "username": mail,
            "password": password
        }
    }
    if website_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="Empty Fields", message="Please insert some data.")
        return
    is_ok = messagebox.askokcancel(title="Save Data?",message="Are you sure you wanna save the data?")
    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0,END)
            messagebox.showinfo(title="Data SAVED", message="Data SAVED")
# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(pady=20, padx=20, bg="white")

canvas = Canvas(bg="white")
canvas.config(highlightthickness=0, width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=bg_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT, bg="white")
website_label.grid(row=1, column=0)
website_input = Entry(font=FONT)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=1, sticky="ew", padx=20, pady=2)
mail_label = Label(text="Email/Username:", font=FONT, bg="white")
mail_label.grid(row=2, column=0)
mail_input = Entry(font=FONT)
mail_input.insert(END,"julia@gmail.com")
mail_input.grid(row=2, column=1, columnspan=2, sticky="ew", padx=20, pady=2)
password_label= Label(text="Password:", font=FONT, bg="white")
password_label.grid(row=3, column=0)
password_input = Entry(font=FONT)
password_input.grid(row=3, column=1, sticky="ew", padx=20, pady=2)
create_password_button = Button(text="Generate Password",font=FONT,command=generate_password)
create_password_button.grid(row=3, column=2, padx=20, pady=2)
add_button = Button(text="Add",font=FONT, command= lambda: save_password(website_input.get(), mail_input.get(), password_input.get()))
add_button.grid(row=4, column=1, columnspan=3, sticky="ew", padx=20, pady=2)
search_button = Button(text="Search",font=FONT,command= lambda: search_data(website_input.get()))
search_button.grid(row=1, column=2, columnspan=1, sticky="ew", padx=20, pady=2)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.maxsize(root.winfo_width(), root.winfo_height())
root.mainloop()
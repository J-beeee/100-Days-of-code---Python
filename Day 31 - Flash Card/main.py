
from tkinter import *
import random
import pandas as pd
from tkinter import messagebox
import os

# ---------------------------- GLOBALS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LIST_ITEM = {}
to_learn = []
# ---------------------------- AUTO FLIP ------------------------------- #
def auto_flip():
    card.itemconfig(language, text="English",fill="white")
    card.itemconfig(vocabulary, text=LIST_ITEM["English"],fill="white")
    card.itemconfig(card_image, image= card_picture_back)
# ---------------------------- BUTTON FUNCTION PANDAS ------------------------------- #
def random_word():
    global LIST_ITEM , flip_timer , to_learn
    data = None
    try:
        data = pd.read_csv(r"data\words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv(r"data\french_words.csv")
    finally:
        try:
            to_learn = data.to_dict(orient="records")
        except AttributeError:
            messagebox.showinfo(title="finished", message="You learned all words")
            os.remove(r"data\words_to_learn.csv")
            messagebox.showinfo(title="finished", message="List deleted")
            random_word()
            return
    root.after_cancel(flip_timer)
    LIST_ITEM = random.choice(to_learn)
    card.itemconfig(language, text="French", fill="black")
    card.itemconfig(vocabulary, text=LIST_ITEM["French"], fill="black")
    card.itemconfig(card_image, image=card_picture)
    # noinspection PyTypeChecker
    flip_timer = root.after(3000, auto_flip)

def wrong():
    random_word()

def right():
    for item in to_learn:
        if LIST_ITEM == item:
            to_learn.pop(to_learn.index(item))
    pd.DataFrame(to_learn).to_csv(r"data\words_to_learn.csv", index=False)
    random_word()

# ---------------------------- GUI ------------------------------- #
root = Tk()
root.config(bg=BACKGROUND_COLOR, pady=50 , padx=50)
root.title("Flash Card")

card_picture = PhotoImage(file=r"images\card_front.png")
card_picture_back = PhotoImage(file=r"images\card_back.png")
card = Canvas( width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263,image= card_picture)
card.grid(row=0, column=0, columnspan=2)

language = card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
vocabulary = card.create_text(400, 363, text="Word", font=("Ariel", 60, "bold"))


button_yes = Button()
right_picture = PhotoImage(file=r"images\right.png")
button_yes.config(image=right_picture, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, overrelief="sunken", activebackground="#B1DDC6", command=right)
button_yes.grid(row=1, column=1)

button_no = Button()
wrong_picture = PhotoImage(file=r"images\wrong.png")
button_no.config(image=wrong_picture, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, overrelief="sunken", activebackground="#B1DDC6", command=wrong)
button_no.grid(row=1, column=0)

# noinspection PyTypeChecker
flip_timer = root.after(3000,func=auto_flip)
random_word()

root.mainloop()
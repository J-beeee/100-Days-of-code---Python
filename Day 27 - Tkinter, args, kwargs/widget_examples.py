import tkinter
from tkinter import IntVar
url = r'https://www.tcl-lang.org/man/tcl8.6/TkCmd/contents.htm'

class Button:
    def __init__(self):
        pass
    def click_button(self, user_text):
        top_label["text"] = user_text
button_function = Button()
window = tkinter.Tk()
window.title("Calc")
window.minsize(width=300, height=200)
window.maxsize(width=1100, height=1100)

#Label
top_label = tkinter.Label(text="I AM a Label!", font=("Arial", 12, "bold"))
top_label.pack(anchor="w")
top_label["text"]= "new Text"
top_label.config(text="new Text 2")
top_label.config(background="green", width=30, height=2, justify="left")

user_input = tkinter.Entry(width=20, borderwidth=2)
user_input.pack(anchor="w", )
user_input.insert(tkinter.END, string="Write Something")

button = tkinter.Button(text="click me",command= lambda: button_function.click_button(user_input.get()))
button.pack(anchor="e")

text = tkinter.Text(height=5, name="test text")
text.pack()
text.insert(tkinter.END, "Example of some text.")
print(text.get("1.0", tkinter.END))

spinbox = tkinter.Spinbox(from_=0, to=10, width=5)
spinbox.pack()

scale = tkinter.Scale(from_=0, to=100)

check_state = IntVar()
checkbutton = tkinter.Checkbutton(text="Ja", variable=check_state)
checkbutton.pack()

radio_state = IntVar()
radiobutton1 = tkinter.Radiobutton(text="option1", value=1, variable=radio_state)
radiobutton1.pack()
radiobutton2 = tkinter.Radiobutton(text="option2", value=2, variable=radio_state)
radiobutton2.pack()

def listbox_used(event):
    selection = listbox.curselection()
    if selection:  # prüft, ob was ausgewählt ist
        print(listbox.get(selection))

fruits = ["apple", "pear", "orange", "banana"]
listbox = tkinter.Listbox(height=4)
listbox.pack()
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
#positionmanage
#.place(x=1,y=0)
#.grid(column= 1, row = 2)
window.mainloop()
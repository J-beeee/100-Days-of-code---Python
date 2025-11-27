import tkinter

window = tkinter.Tk()
window.title("My second GUI Program")
window.minsize(width=500, height=300)
window.config(padx=5, pady=5)
label_one = tkinter.Label(text="Label")
label_one.config(font=("Arial", 24, "bold"))
label_one.grid(column=0, row=0)

new_button = tkinter.Button(text="new_button")
new_button.config(font=("Arial", 24, "bold"),padx=5, pady=5)
new_button.grid(column=2, row=0)

button = tkinter.Button(text="button")
button.config(font=("Arial", 24, "bold"),padx=5, pady=5)
button.grid(column=1, row=1)

entry = tkinter.Entry()
entry.config(font=("Arial", 24, "bold"))
entry.insert(tkinter.END, "Please write here.")
entry.grid(column=3, row=3)





window.mainloop()
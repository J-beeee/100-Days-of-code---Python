import tkinter
pad = 5
def calculate():
    km_output = float(miles_insert.get())* 1.609
    label_two["text"] = km_output

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
window.maxsize(300, 200)


miles_insert = tkinter.Entry(width=7)
miles_insert.grid(row=0, column=1, padx=pad, pady=pad)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2, padx=pad, pady=pad)

label_one = tkinter.Label(text="is equal to")
label_one.grid(row=1, column=0, padx=pad, pady=pad)

label_two = tkinter.Label()
label_two.grid(row=1, column=1, padx=pad, pady=pad)

label_three = tkinter.Label(text="Km")
label_three.grid(row=1, column=2, padx=pad, pady=pad)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1, padx=pad, pady=pad)

window.mainloop()
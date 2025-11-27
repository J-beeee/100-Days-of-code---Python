import tkinter

class Button:
    def __init__(self):
        self.button_click_counter = 0
    def button_clicked(self, label):
        if self.button_click_counter >= 1:
            self.button_click_counter += 1
            label["text"] = f"Button got clicked {self.button_click_counter} times!"
        else:
            label["text"]="Button got clicked!"
            self.button_click_counter += 1

my_button_function = Button()
window = tkinter.Tk()
window.title("My second GUI Program")
window.minsize(width=500, height=300)



#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"]="new Text"
my_label.config(text="I Am a Label!")



button = tkinter.Button(text="Click Me!", command= lambda: my_button_function.button_clicked(label=my_label))
button.pack()




#def add(*args):
#    x = 0
#    for num in args:
#        x += num
#        print(x)
#add(1,2,3,4)
#def calculate(n, **kwargs):
    #print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    #print(kwargs["add"])
    #print(kwargs["multiply"])
    #n += kwargs["add"]
    #n *= kwargs["multiply"]
    #print(n)

#calculate(2,add=3, multiply=2)
#
#
#class Car:
#    def __init__(self, **kwargs):
#        self.make = kwargs["make"]
#        self.model = kwargs.get("model")
#        self.color = kwargs.get("color")
#
#my_car = Car(make="Nissan", model="GT-R")
#print(my_car.model)
#print(my_car.color)



window.mainloop()
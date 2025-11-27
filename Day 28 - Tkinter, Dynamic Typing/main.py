import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    # noinspection PyTypeChecker
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="Timer")
    reps = 0
    bottom_label.config(text="")
    start_button.config(state="active")
    reset_button.config(state="disabled")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    start_button.config(state="disabled")
    reset_button.config(state="active")

    if reps % 8 == 0:
        count_down(long_break_sec)
        top_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        top_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        top_label.config(text="WORK", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        worker_session = math.floor(reps/2)
        for _ in range(worker_session):
            mark += "✓"
        bottom_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



top_label = Label()
top_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
top_label.grid(column=1, row=0)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(102,112,image= tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button()
start_button.config(text="Start", font=(FONT_NAME, 12, "bold"), fg="black", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text="Reset", font=(FONT_NAME, 12, "bold"), fg="black", bg="white", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

bottom_label = Label()
bottom_label.config(font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
bottom_label.grid(column=1, row=3)

window.update()
window.minsize(window.winfo_width(), window.winfo_height())
window.maxsize(window.winfo_width(), window.winfo_height())
window.mainloop()

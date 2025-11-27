import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.root = tkinter.Tk()
        self.root.title("Quiz App")
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row = 0, column = 1)

        self.canvas = tkinter.Canvas(self.root, width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            fill=THEME_COLOR,
            text="Hier steht die Frage.",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        yes_pic = tkinter.PhotoImage(file=r"images\true.png")
        self.button_yes = tkinter.Button(image=yes_pic)
        self.button_yes.config(
            highlightthickness=0,
            borderwidth=0,
            bg=THEME_COLOR,
            overrelief="sunken",
            activebackground=THEME_COLOR,
            command= self.button_right

        )
        self.button_yes.grid(row=2, column=0)
        no_pic = tkinter.PhotoImage(file=r"images\false.png")
        self.button_no = tkinter.Button(image=no_pic)
        self.button_no.config(
            highlightthickness=0,
            borderwidth=0,
            bg=THEME_COLOR,
            overrelief="sunken",
            activebackground=THEME_COLOR,
            command=self.button_false
        )
        self.button_no.grid(row=2, column=1)

        self.next_question()

        self.root.mainloop()
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text= q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_no.config(state="disabled")
            self.button_yes.config(state="disabled")

    def button_right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def button_false(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.next_question)


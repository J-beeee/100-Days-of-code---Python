from data import question_data
from quiz_brain import QuizBrain
is_done = False
quiz = QuizBrain(question_data)

while not is_done:
    is_done = quiz.q_used()
    if is_done:
        print("Quiz done.")
        break
    quiz.next_question()

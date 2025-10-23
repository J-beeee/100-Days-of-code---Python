import random
class QuizBrain:

    def __init__(self, question_data):
        self.question_number = 0
        self.question_list = question_data
        self.question = None
        self.used_questions = []
        self.score = 0

    def q_used(self):
        if len(self.used_questions) == len(self.question_list):
            return True, print(f"You've completed the quiz.\nYour final score was: {self.score}/{self.question_number}")
        self.question = random.choice(self.question_list)
        while self.question in self.used_questions:
            self.question = random.choice(self.question_list)

        self.used_questions.append(self.question)
        return False
    def next_question(self):
        current_question = self.question
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question["text"]} (True/False]: ')
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.question["answer"].lower():
            self.score += 1
            print(f"You got it right!\nThe correct answer is {self.question["answer"]}\nYour score: {self.score}/{self.question_number}")
        else:
            print(f"Wrong answer!\nThe correct answer is {self.question["answer"]}\nYour score: {self.score}/{self.question_number}\n")

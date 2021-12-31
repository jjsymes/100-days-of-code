from tkinter import *
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

directory = os.path.realpath(__file__ + f"/{os.pardir}")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_tracker = Label(text="Score: 0", bg=THEME_COLOR, pady=20)
        self.score_tracker.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.question_canvas.create_text(150, 125, text=f"This is a question", fill=THEME_COLOR, width=280, font=("Arial", 20, "italic"))

        true_image = PhotoImage(file=f"{directory}/images/true.png")
        false_image = PhotoImage(file=f"{directory}/images/false.png")

        self.true_button = Button(command=self.submit_true, bg=THEME_COLOR, image=true_image)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false_button = Button(command=self.submit_false, bg=THEME_COLOR, image=false_image)
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=question)
        else: 
            self.finish_quiz()

    def submit_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        self.window.after(1000, self.get_next_question)

    def submit_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        self.window.after(1000, self.get_next_question)

    def give_feedback(self, is_right):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.score_tracker.config(text=f"Score: {self.quiz.score}")
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.reset_feedback)

    def reset_feedback(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.question_canvas.config(bg="white")

    def finish_quiz(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.question_canvas.itemconfig(self.question_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
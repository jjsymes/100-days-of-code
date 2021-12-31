from utils import get_user_choice

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        ui_question_text = f"Q.{self.question_number}: {question.text} (True/False)?: "
        player_answer = get_user_choice(ui_question_text, ["true", "false", "t", "f"])
        correct_answer = question.answer
        self.check_answer(player_answer, correct_answer)

    def check_answer(self, player_answer, correct_answer):
        if player_answer[0].lower() == correct_answer[0].lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

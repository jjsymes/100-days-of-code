import requests
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from utils import unescape_html_in_dictionary

question_bank = []

# Get questions from data.py
for question in question_data:
    question_text = question.get("text")
    question_answer = question.get("answer")
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Get questions from Open Trivia DB
question_api_url = "https://opentdb.com/api.php?amount=12&type=boolean"
response = requests.get(question_api_url)
if response and response.status_code == 200:
    json_data = response.json()
else:
    json_data = None

if json_data:
    unescape_html_in_dictionary(json_data)
    question_bank = []
    for question in json_data.get("results"):
        question_text = question.get("question")
        question_answer = question.get("correct_answer")
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)



# Play game
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
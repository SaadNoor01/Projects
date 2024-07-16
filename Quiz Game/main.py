from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    new_question = Question(x["question"], x["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.ask_question()

print(f"You have completed the quiz\nYour final score is: {quiz_brain.score}/{quiz_brain.question_number}")

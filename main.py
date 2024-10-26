from question_model import Question
from data import question_data
from quiz_game import QuizGame

question_bank = []
for question in question_data:
    question_bank = Question["text"]
    question_bank =  Question["answer"]
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print("your final score was:{quiz.score}/{quiz.question_number}")

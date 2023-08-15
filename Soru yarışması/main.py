from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain
veri = question_data
question_bank = []
for i in veri:
    a = i
    soru = a["text"]
    cevap = a["answer"]
    new_question= Question(soru,cevap)
    question_bank.append(new_question)
quiz = Quiz_brain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
if quiz.question_number == 12:
    print("You've completed the quiz.")
    score = quiz.score
    print(f"Your final score was {score}/{quiz.question_number}")
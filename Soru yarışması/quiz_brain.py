class Quiz_brain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        mevcut_soru = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q. {self.question_number}: {mevcut_soru.text} (True/False) : ")
        self.check_answer(user_answer,mevcut_soru.answer)

    def check_answer(self,user_answer,answer):
        if user_answer.lower() == answer.lower():
            self.score +=1
            print("You got it right!")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("That's wrong")
            print(f"Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer {answer}")
        print("")
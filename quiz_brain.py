class Quiz_brain:

    def __init__(self):
        self.questions_number = 0
        self.question_list = q_list

    def still_has_questions(self):
       return self.questions_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.questions_number]
        self.questions_number += 1
        user_answer = input(f"Q.{self.questions_number}: {current_question}(true/false):")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you are correct")
        else:
            print("you are wrong")
        print(f"te correct answer was: {correct_answer}.")
        print(f"your current score was: {self.score}/{self.questions_number}")
        print("/n")
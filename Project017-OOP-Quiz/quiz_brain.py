class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower().strip()
            if user_input == "true" or user_input == "false":
                break
            else:
                print("Please enter either True or False!")

        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, answer):

        user_answer = user_input
        correct_answer = answer

        if user_answer == correct_answer:
            self.score += 1
            print("You're correct!")
        else:
            print("That's incorrect!")

        print(f"The correct answer was '{correct_answer}'")
        print(f"Your score: {self.score}/{self.question_number}\n\n")

    def display_score(self):
        print("You've completed the quiz")
        print(f"Your final score: {self.score}/{self.question_number}")

class Question:
    def __init__(self, questionTxt, answ_1, answ_2, answ_1_people, answ_1_wealth, answ_2_people, answ_2_wealth):
        self.questionTxt = questionTxt
        self.answ_1 = answ_1
        self.answ_2 = answ_2
        self.answ_1_people = int(answ_1_people)
        self.answ_1_wealth = int(answ_1_wealth)
        self.answ_2_people = int(answ_2_people)
        self.answ_2_wealth = int(answ_2_wealth)

    def debug(self):
        print("QuestionTxt:", self.questionTxt)
        print("answ_1:", self.answ_1)
        print("answ_2:", self.answ_2)
        print("answ_1_people:", self.answ_1_people)
        print("answ_1_wealth:", self.answ_1_wealth)
        print("answ_2_people:", self.answ_2_people)
        print("answ_2_wealth:", self.answ_2_wealth)
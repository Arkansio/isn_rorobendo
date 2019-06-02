from Tkinter import *

class Question_window:
    def showStats(self, nb_people, nb_wealth):
        text1 = "Peuple : " + str(nb_people[0])
        text2 = "Richesse : " + str(nb_wealth[0])
        champ_label1 = Label(self.window, text=text1)
        champ_label1.pack()
        champ_label2 = Label(self.window, text=text2)
        champ_label2.pack()

    def __init__(self, question, nb_people, nb_wealth, response):
        self.window = Tk()
        self.choice = IntVar()
        self.choice = response

        self.showStats(nb_people, nb_wealth)
        champ_label1 = Label(self.window, text="la question du mois est : ")
        champ_label1.pack()
        champ_label2 = Label(self.window, text=question.questionTxt)
        champ_label2.pack()
        choix_a = Radiobutton(self.window, text=question.answ_1, variable=self.choice[0], value=0)
        choix_b = Radiobutton(self.window, text=question.answ_2, variable=self.choice[0], value=1)
        choix_a.select()
        choix_a.pack()
        choix_b.pack()
        SubmitButton= Button(self.window,text= 'CHOISIR', command=self.handlerSubmit)
        SubmitButton.pack()
        self.window.mainloop()

    def handlerSubmit(self):
        self.window.destroy()
        
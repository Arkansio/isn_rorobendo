import numpy as np

verbose = 0

def read_file_questions(Q) :
    A=open("questions.txt",'r')
    line = A.readline().split(";")
    while line != [''] :
        Q.append(line[:-1])
        line = A.readline().split(";")
        #print ('le texte : ', line)
    A.close()

def read_file_effects(E) :
    A=open("effets.txt",'r')
    line = A.readline().split(";")
    while line != [''] :
        E.append(line[:-1])
        line = A.readline().split(";")
        #print ('les effets : ', line)
    A.close()


def createIndexTab(qst_tab) :
    newTab = np.arange(0, len(qst_tab))
    np.random.shuffle(newTab)
    return (newTab)

def getQuestion(index_tab):
    i = index_tab[0]
    return (i)

def deleteQuestion(index_tab):
    newTab = index_tab = np.delete(index_tab, [0])
    return (newTab)

def readChoice():
    while (1):
        res = input()
        if (res.strip() == "a"):
            return (0)
        elif (res.strip() == "b"):
            return (1)

def game () :
    qst_tab = []
    read_file_questions(qst_tab)
    if (verbose):
        print ('le texte :', qst_tab[0])

    eff_tab = []
    read_file_effects(eff_tab)
    if (verbose):
        print ('les effets :', eff_tab)

    index_tab = createIndexTab(qst_tab)
    if (verbose):
        print(index_tab)

    nb_people = 25
    nb_wealth = 25
    while (len(index_tab)):
        print("Peuple:", nb_people)
        print("Richesse:", nb_wealth)

        qst_index = getQuestion(index_tab)
        index_tab = deleteQuestion(index_tab)

        qst_entity = qst_tab[qst_index]
        qst_text = qst_entity[0].strip()
        qst_choice_a = qst_entity[1].strip()
        qst_choice_b = qst_entity[2].strip()

        print("\nLa question du mois est :")
        print(qst_text)
        print("a)", qst_choice_a)
        print("b)", qst_choice_b)
        
        choice = readChoice()


game()
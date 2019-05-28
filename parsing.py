import random
from question import Question

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

def parseQuestions():
    # Creation d'un tableau vide
    questions = []

    # Lecture du fichiers des questions
    qst_tab = []
    read_file_questions(qst_tab)
    if (verbose):
        print ('le texte :', qst_tab[0])

    # Lecture du fichiers des effets
    eff_tab = []
    read_file_effects(eff_tab)
    if (verbose):
        print ('les effets :', eff_tab)

    # On convertit les questions et les effets dans une seule classe
    i = 0
    while i < len(qst_tab):
        q = qst_tab[i]
        e = eff_tab[i]

        newQuestion = Question(q[0], q[1], q[2], e[0], e[1], e[2], e[3])
        questions.append(newQuestion)

        i += 1
    
    # On melange les questions
    random.shuffle(questions)
    
    return (questions)
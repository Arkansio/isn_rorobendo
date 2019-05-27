import numpy as np

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
    np.delete(index_tab, 0)
    return (i)

def game () :
    qst_tab = []
    read_file_questions(qst_tab)
    print ('le texte :', qst_tab[0])

    eff_tab = []
    read_file_effects(eff_tab)
    print ('les effets :', eff_tab)

    index_tab = createIndexTab(qst_tab)
    print(index_tab)

    qst_index = getQuestion(index_tab)

    print("La question du mois est : \n", qst_tab[qst_index][0])

game()
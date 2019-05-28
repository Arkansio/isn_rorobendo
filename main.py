from parsing import parseQuestions

verbose = 0
# Recuperer la question et la supprimer du tableau
def getQuestion(questions):
    i = questions[0]
    questions.pop(0)
    return (i)

# Lire sur l'entree standard le choix du joueur
def readChoice():
    while (1):
        res = input()
        if (res.strip() == "a"):
            return (0)
        elif (res.strip() == "b"):
            return (1)

# Check si on est dans les limites (peuple, richesse)
def checkDead(p, w):
    return (p <= 0 or p >= 50 or w <= 0 or w >= 50)

# Appliquer l'effet
def applyEffect(nb_people, nb_wealth, question, choice):
    if (choice):
        nb_people[0] += question.answ_2_people
        nb_wealth[0] += question.answ_2_wealth
    else:
        nb_people[0] += question.answ_1_people
        nb_wealth[0] += question.answ_1_wealth

# Afficher le dilemne
def showMonthQuestion(question):
    print("\nLa question du mois est :")
    print(question.questionTxt)
    print("a)", question.answ_1)
    print("b)", question.answ_2)

def game () :
    # On charge les questions
    questions = parseQuestions()

    # Initialisation des variables de depart
    dead = 0
    nb_people = [25]
    nb_wealth = [25]

    # Tant qu'on n'est pas mort et qu'il reste des questions
    while (len(questions) and not dead): 
        print("Peuple:", nb_people[0])
        print("Richesse:", nb_wealth[0])

        # Recuperer la fonction et la supprimer du tableau
        question = getQuestion(questions) 
        if (verbose):
            question.debug()

        # Afficher le dilemne
        showMonthQuestion(question) 
        
        # Recuperer le choix
        choice = readChoice()

        # Appliquer l'effet de la question
        applyEffect(nb_people, nb_wealth, question, choice) 
        
        # Check si on est dans les limites (peuple, richesse)
        if (checkDead(nb_people[0], nb_wealth[0])): 
            dead = 1

    # yes la meuf est dead
    if (dead): 
        print("t mort pas dchance lol")

game()
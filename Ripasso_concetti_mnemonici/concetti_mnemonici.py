import random
import re

quiz = False
add = False
a=0

check_switch=input("Vuoi fare un quiz o inserire nuove domande?1 o 2\n")
if check_switch == "1":
    quiz = True
if check_switch == "2":
    add = True

while True:
    while quiz:
            file_domande = open("domande.txt", "r")
            file_risposte = open("risposte.txt", "r")

            domande = file_domande.readlines()
            risposte = file_risposte.readlines()

            file_domande.close()
            file_risposte.close()

            x = random.randint(0,len(domande)-1)
            
            
            domanda = domande[x].replace("\n", "")
            risposta = risposte[x].replace("\n", "")

            print(f"{domanda}") 

            if (str(input("Inserire risposta: "))) == (risposta):
                print("Bravo è corretto")
            else:
                print(f"La risposta era {risposta}")
            
            check = input("\nSe vuoi fermarti premi \'.\'\n")       
            if (check == "."):
                check_switch = input ("\nVuoi aggiungere domande al database? Y/n\n")
                if (check_switch == "Y" or check_switch == "y"):
                    add = True
                    quiz = False
                else:
                    a=1
                    break 

    while add:
        file_domande = open("domande.txt", "a")
        file_risposte = open("risposte.txt", "a")
        QW = True
        AW = True
        while QW:
            domanda = (input("Inserisci nuova domanda: "))
            check3 = input("Sei sicuro di volerla aggiungere?Y/n\n")
            if check3 == "Y" or check3 == 'y':
                file_domande.write(domanda + '\n')
                QW = not QW

        while AW:
            risposta=(input("Inserisci risposta:  "))
            check4 = input("Sei sicuro di volerla aggiungere?Y/n\n")
            if check4 == "Y" or check4 == 'y':
                file_risposte.write(risposta + '\n')
                AW = not AW
            
        check = input("\nSe vuoi fermarti premi \'.\'\n")       
        if (check == "."):
            check_switch = input ("\nVuoi iniziare un nuovo quiz? Y/n\n")
            if (check_switch == "Y" or check_switch == "y"):
                add = False
                quiz = True
            else:
                a = 1
                break
    if (a==1):
        break

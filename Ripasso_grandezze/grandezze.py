import random

while True:
    file_domande = open("grandezze_domande.txt", "r")
    file_risposte = open("grandezze_risposte.txt", "r")

    domande = file_domande.readlines()
    risposte = file_risposte.readlines()

    file_domande.close()
    file_risposte.close()

    x = random.randint(0, len(domande))

    domanda = domande[x].replace("\n", "")
    risposta = risposte[x].replace("\n", "")

    print(f"Inserisci unità di misura, simbolo e grandezze primitive(qualora sia possibile) di {domanda}: ")

    if (str(input("Inserire risposta: "))) == (risposta):
        print("Bravo è corretto")
    else:
        print(f"La risposta era {risposta}")

    check = input("\nSe vuoi fermarti premi \'.\'\n")       
    if (check == "."):
            break

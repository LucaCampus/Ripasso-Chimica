import random
import re



while True:
        file_domande = open("elementi_5_6.txt", "r")
        file_risposte = open("risposte_5_6.txt", "r")

        domande = file_domande.readlines()
        risposte = file_risposte.readlines()

        file_domande.close()
        file_risposte.close()

        x = random.randint(0,len(domande)-1)
        
        domanda = re.sub("\n", "", domande[x])
        risposta = re.sub("\n", "", risposte[x])

        print(f"Inserisci simbolo, stato di aggregazione, categoria, numero di ossidazione e gruppo di {domanda}") 

        if (str(input("Inserire risposta: "))) == (risposta):
            print("Bravo è corretto")
        else:
            print(f"La risposta era {risposta}")
        
        check = input("\nSe vuoi fermarti premi \'.\'\n")       
        if (check == "."):
            break

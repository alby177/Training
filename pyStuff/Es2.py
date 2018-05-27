contatore = 0
continua = False
if contatore < 10:
    print(contatore)
    contatore +=1
    
print("Ora passo al while")

while contatore < 20:
    print(contatore)
    contatore += 1
    if contatore == 12:
        print("I'm out")
        if continua == True:
            continue # continua il ciclo, esegue l'istruzion corrente ma senza poi eseguire ciò che viene dopo, ricomincia il ciclo dal passo successivo
            print("Scherzavo")
        else:
            break
print("Ora sono davvero fuori")

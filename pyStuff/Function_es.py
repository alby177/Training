def print_tre_volte(): #come definire il nome della funzione personalizzata che vado a creare, dentro le parentesi posso mettere parametri
    print('Ciaone') #il coddice della funzione va indentato dopo la definizione
    print('Ciaone')
    print('Ciaone')

print_tre_volte() # la funzione va richiamata o qui o da riga di comando per farla girare

def sommatrice(a, b):
    print('Questa è la funzione somma')
    print('Fornisce la somma di due numeri passato come parametri')
    risultato = a + b
    print('il risultato della somma è ' +str(risultato))

def laptop_nuovo(ram, cpu, antivirus = False):
    print('Il nuovo laptop avrà le seguenti carattersistiche: ')
    print('Ram ' + ram)
    print('Cpu ' + cpu)
    if antivirus == True:
        print('Abbiamo un antivirus')

def moltiplicatrice(a, b):
    risultato = a * b
    return(risultato) # ritorna la variabile contenuta all'interno delle parentesi, se richiamata da shell la stampa a video, altrimenti salva il valore
                      # nella variabile a cui viene messa uguale la funzione

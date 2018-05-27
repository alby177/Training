elenco = [2, 5, 'Ciccio', 3.14, 'eggs']
print(elenco)
print(elenco[0]) # accedo ad un elemento della lista, ordinati da sinistra verso destra
print(elenco[-2]) #accedo ad un elemento della lista, ordinati da destra verso sinistra

primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(primi[3:9]) # stampa dall'elemento 3 al 9
sottoinsieme = primi[3:6]
print(sottoinsieme)

print(primi[4:]) # stampa dal 5 elemento (perchè parte da 0) fino alla fine
print(primi[:4]) # stampa dall'elemento 0 fino a dove gli viene detto

for primo in primi: # posso far iterare seguendo i numeri interni alla lista definita
    print(primo)

listaNumerica = list(range(99,300)) # tramite la funzione list posso creare una lista a convertendo il range ad esempio osì verranno inclusi tutti i numeri dal valore minimo al massimo
print(listaNumerica)

listaMultipla = ['Spam', 'ciao', 21, 4, 'ahia', [1, 2, 3, 4], 23]
print(listaMultipla[-2]) # accedo alla sottolista all'interno della lista richimando la posizione della sottolista nella lista
print(listaMultipla[-2][2]) # stampo il valore 2 della sottolista che si trova alla posizione -2 o 4 della lista principale
listaMultipla[-2][2] = 'Culo'
del listaMultipla[-2][3] # cancella l'elemento della posizione corrispondente nella lista
print(listaMultipla)


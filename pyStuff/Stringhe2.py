nome = 'Jack'
print('ciao ' + nome)

numero = 18
print('Questa è la serie numero', numero)

print(f"ciao {nome}, questa è la lazione n°{numero}! Magia") # inserire la 'f' davanti mi permette  di fare una striga formattata e quindi sfruttare la cnversione automatica delle variabili

z = 5
print(f'Il quadrato di {z} è {z**2}')

messaggio = 'Fate il vostro gioco'
print(messaggio.startswith('Fate il')) # mi dice se la stringa comincia con le lettere pasate come parametro
print(messaggio.startswith('F')) #vale da un carattere a delle stringhe intere

print(messaggio.endswith('f')) # mi dice se la stringa finisce con le lettere pasate come parametro
print(messaggio.endswith('gioco')) # mi dice se la stringa finisce con le lettere pasate come parametro

nome = 'alice'
print(nome.islower()) # mi dice se la stringa è scritta tutta in minuscolo

cognome = 'BACCO'
print(cognome.isupper()) # mi dice se la stringa è scritta tutta in maiuscolo

lettere = 'ciAonE'
print(lettere.islower())
print(lettere.isupper())

print(lettere.upper()) # riscrive tutta la stringa in maiuscolo
print(lettere.lower()) # riscrive tutta la stringa in minuscolo
# non modifica la stringa ma ne stampa una nuova, la stringa di partenza resta come è stata scritta
print(lettere)
lettere = lettere.upper() # così modifico la stringa di base
print(lettere)

print(lettere.isalpha()) # mi dice se la parola è composta solo da lettere
parola = '12'
print(parola.isdecimal()) # mi dice se la parola è composta solo da numeri
parola2 = 'asd12'
print(parola2.isalnum()) # mi dice se la stringa è composta da soli lettere o numeri (es. no spazi)

parola3 = '123allora '
print(parola3.isalnum())
#da False perchè c'è dentro uno spazio

eggs = '@adsadasd3434324234234?323!'
stringaNuova = ''
for carattere in eggs: #voglio tenere i caratteri che siano lettere o numeri e buttare via il resto
    if carattere.isalnum() == True:
        stringaNuova += carattere
print(stringaNuova)

print(parola3[9].isspace()) # ritorna True se il carattere selezionato è uno spazio
print(parola3.isspace()) # essendo una stringa non solo di spazi mi ritorna False

compiti = ['protare il cane a passeggio','finire di studiare','lavare i piatti', 'fare la spesa']
print(', '.join(compiti)) # permette di inserire il pezzo di stringa ad ogni ingresso della lista e stamparla come se fosse una frase consecutiva

daFare = 'oggi devo:\n' + ',\n'.join(compiti)
print(daFare)

serieNumerica = '1492-1984-123-43545-3331'
print(serieNumerica.split('-')) # divide la stringa in una lista, andando a dividere basandosi sul carattere passato come parametro

#TUTTI QUESTI METODI, NON MODIFICANO LA VARIABILE DI PARTENZA MA FANNO LE MODIFICHE SU UNA VARIABILE TEMPORANEA PER CUI SE VOGLIO
#TENERE IL VALORE DEVO SALVARLO NELLA STESSA O IN UN ALTRA VARIABILE

citazione = 'Nel mezzo del cammin di nostra vita'
print(citazione.split(' '))


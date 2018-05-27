# i dizionari sono composti da una chiave (prima dei due punti) e un valore (dopo i :). Sono liste a cui invee di associare un indice, si associano delle chiavi che fanno lo stesso lavoro dell'indice ma gli ci si può dare un qualsiasi valore. 
mioDizionario = {'miaChiaveUno' : 'mioValoreUno', 'età' : 24, 3.14: 'piGreco', 'primi':[1,2,3,5,7]}
print(mioDizionario['età']) # richiama il valore corrispondente alla chiave età all'interno del dizionario mioDizionario

mioDizionario['NuovaChiave'] = 'NuovoValore' # aggiungo una chiave e il suo corrispondente valore

mioDizionario['età'] = 95 # sosituisco il valore corrispondente alla chiave 'età'

# i Dizionari sono elenchi di chiave valore non ordinati, per cui anche se sono in ordine diverso, python li legge come uguali

print('miaChiaveUno' in mioDizionario) #cerca un valore o una chiave all'interno del dizionario
print('dodici' not in mioDizionario) #cerca se non è presente una hiave o un valore all'interno di un dizionario

del mioDizionario['miaChiaveUno'] #cancella un elemento all'interno del dizionario
print(mioDizionario)

itaEng = {'Ciao' : 'Hello', 'Arrivederci' : 'Goodbye', 'Uova' : 'Eggs', 'Gatto' : 'Cat', 'Arancia' : 'Orange'}
print(itaEng.keys()) # restituisce tutte le chiavi presenti nel dizionaro
print(itaEng.values()) # restituisce tutte i valori presenti nel dizionaro
print(itaEng.items()) # restituisce tutte le coppie chiavi valore presenti nel dizionaro

paroleEng = list(itaEng.values())
print(paroleEng)

for chiave in itaEng.keys(): #stampa tutte le keys in ordine perchè assegna le chiavi alla variabile 'chiavi' che viene poi stampata dal ciclo, così accedo ad ogni chiave
    print(chiave)

if 'birra' in itaEng.keys():
    print(itaEng['birra'])
else:
    print('Chiave non trovata')

itaEng.get('Ciao', 'Chiave non trovata!') # restituisce il valore relativo alla chiave indicata se la chiave esiste
itaEng.get('Birra', 'Chiave non trovata!') # resitituisce la stringa inserita se la chiave non esiste
#sembra funzionare solo da riga di comando

itaEng.setdefault('Birra','Beer') # tramite questo metodo inserisco la coppia chiave valore al fondo del dizionario, priam cerca se eseiste e se non esiste allora lo inserisce.
# Se esiste allora restituisce il valore relativo alla chiave inserita, anche se il valore non è quello presente nel dizionario






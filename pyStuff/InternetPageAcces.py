import requests, bs4 # importo i moduli requests per l'acquisizione delle pagine web e bs4 che trasforma la pagina html in un oggetto
# acquisizione pagina web, bisogna dirgli che tipo di applicazione si sta connettendo al server altrimenti il server mi nega l'accesso
# Qui ho impostato che mi connetto come Mozilla ma anche se non è così non importa, l'importante è specificare un'applicazione
res = requests.get('https://www.packtpub.com', headers={'user-agent' : 'Mozilla/5.0'})
res.raise_for_status() # controlla se c'è stato qualche errore durante l'acquisizione del sito web
packtpub = bs4.BeautifulSoup(res.text, "html.parser") # creazione dell'oggetto a partire dal codice html, devo anchr indicare il tipo di parser
# altrimenti mi da un warning. Questo è quello standard indicato dall'interprete python di windows
lista = packtpub.select('span') # Seleziona un tipo specifico di TAG html e ritorna una lista degli ogetti trovati
print(lista[0].getText()) # Tramite il metodo getText posso vedere il testo formattato normalmente e non in codice html
print(lista[0]) # Il codice viene visto come HTML
print(lista[0].get('class')) # Cerca l'attributo di tipo "class" all'interno dell'elemento della lista
if lista[0].get('class') != None: # Posso cercare se esiste un attributo classe all'interno della lista
    print("Found!")
else:
    print("Not Found!")
print(lista[0].attrs) # Con il metodo ".attrs" mi ritorna in un dizionario l'attributo come indice e il valore dell'attributo come valore

# Programma per prendere una stringa da linea di comando ed effettuare una ricerca google su quella stringa, aprendo i tab solo dei migliori risultati
import requests, sys, webbrowser, bs4

print("Googling....")
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
# Quando si cerca qualcosa su google lui fa apparire la stringa come scritta sopra, poi io ci metto tutti i caratteri passati da linea di comando
# uno di seguito all'altro ma intervallati da uno spazio (quello tra ' ' è il separatore)
exc = None

try:
    res.raise_for_status() # Controlla se c'è stato un errore durante l'apertura della pagina web
except Exception as exc:
    print("The following exception is occurred:", exc) # Messaggio di errore in caso di eccezione

if exc is None:
    minTabs = int(input("Insert the number of browser tabs to open (if found enough of them): "))

soup = bs4.BeautifulSoup(res.text, "html.parser") # Salva la pagina HTML all'interno dell'oggetto soup

linkElems = soup.select('.r a') # Crea una lista contenente tutti i risultati di ricerca di google
# I risultati si trovano tutti sotto lo stesso tipo di classe r e hanno tutti l'elemento <a>, quindi li si trova in questo modo

numOpen = min(minTabs, len(linkElems)) # Seleziona il numero di tab del browser da aprire, è il minimo tra minTabs inserito dall'utente
# oppure il numero di elemeti trovati

for i in range(numOpen):
    webbrowser.open('http:://google.com/' + linkElems[i].get('href'))
    # Apre il numero di tabs del browser richiesti. All'interno della lista va a prendere solo gli elementi
    # di tipo "href", che sono le URL delle voci di ricerca, in modo da aprirle all'interno del browser

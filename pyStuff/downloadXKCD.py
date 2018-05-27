# Script che accede al sito http://xkcd.com/ e scarica tutti i fumetti che ci sono, usando il tasto prev per
# andare indietro con le pagine e prendere tutto quello che trova
import requests, os, bs4

url = 'http://xkcd.com/' # URL da cui partire per cominciare a scaricare i dati
os.makedirs('xkcd', exist_ok = True) # Crea una cartella o verifica che già ci sia senza mandare eccezioni se già esiste
while not url.endswith('#'): # Sappiamo che l'ultima pagina ha l'indirizzo http://xkcd.com/#, quindi cerchiamo fino a quando non troviamo #

    print("Downloading page {}... ".format(url)) # Stampa l'indirizzo della pagina da cui sta scaricando
    res = requests.get(url) # Apre la pagina
    res.raise_for_status() # Verifica se ci sono errori

    soup = bs4.BeautifulSoup(res.text, 'html.parser') # Crea l'oggetto dalla pagina html
    comicElem = soup.select('#comic img') # Prende tutte gli elementi di classe comic di tipo img
    if comicElem == []:
        print('Could not find the Image! :(')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src') # Recupera la url dell'immagine che si trova sotto il tipo "src" nella apgina html
            #print("Downloading the image: {}...".format(comicElem[0].get('title'))) # Stampa il titolo dell'immagine che si trova sotto il tipo title
            print("Downloading the image from: {}".format(comicUrl))
            resBis = requests.get(comicUrl) # Apre la pagina dell'url dell'immagine
            resBis.raise_for_status()
        except requests.exceptions.MissingSchema: # Se c'è un errore skippa l'immagine corrente
            prevLink = soup.select('a [rel="prev"]')[0] # In caso di errore seleziona il pulsante previous image
            url = 'http://xkcd.com' + prevLink.get('href') # Prende il link legato al pulsante previous image e va all'immagine precedente
            continue

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        # os.path.basename serve per eliminare la parte superflua dell'url lasciando solo il nome dell'immagine salvato nell'url (sembra un po' un path quindi si sfrutta la funzione basename)
        # tramite il comando ".join" gli dico di scrivere il file dopo la virgola (il nome dell'immagine) dentro la cartella xkcd
        # lo apro in scrittura in binary mode in modo da salvare correttamente il file
        for chunk in resBis.iter_content(len(resBis.text)): # tramite l'iteratore della funzione ".iter_content()" salvo l'immagine
            imageFile.write(chunk) # scrivo l'immagine sul file imageFile che ho aperto prima tramite la write dell'elemento chunk iterato tramite iter_content
        imageFile.close() # chiudo il file

    prevLink = soup.select('a[rel="prev"]')[0] # In caso di errore seleziona il pulsante previous image
    url = 'http://xkcd.com' + prevLink.get('href') # Prende il link legato al pulsante previous image e va all'immagine precedente
print("Done!")

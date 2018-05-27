# Write: sovrascrive ciò che c'è all'interno del file di testo mettendo le cose nuove dentro
# Append: aggiunge a ciò che è presente nel file ciò che si invia

contenuto = "Oggi è una bellissima giornata!" # specifico che si tratta di una stringa unicode
file1 = open('esempio1.txt', 'w', encoding='utf-8') # si deve mettere il nome del file da aprire/creare e il modo di apertura
# specificando solo il nome senza percorso lui lo cerca/crea all'interno della cartella dove è salvato il file .py
# specifico il tipo di econding in modo da permettere la scrittura in unicode e non in ASCII (perchè l'ACSII non comprende le lettere accentate e non viene riconosciuto il carattere)

file1.write(contenuto) # scrive la stringa contenuto sul file
file1.close() #chiude il file
# ricordarsi di chiudere sempre il file dopo la scrittura per evitare danni ai dati

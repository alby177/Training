x = 15

def funzioneEsempio():
    global x # permette di modificare una variabile globale, devo farlo consapevolmente dicendogli che sto agendo su una variabile globale
    x += 2
    return(x)

print(funzioneEsempio())


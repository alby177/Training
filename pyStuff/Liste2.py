a = ['1','2','3']
b = [3, 4, 7]

print(a+b)
print(a*3)

print('1' in a) # consente di cercare un elemento all'interno di una lista, restitusce True se c'è altrimenti False

alfa = 'abcdefghi'

def reverser(stringa):
    indice = len(stringa) - 1
    nuovaStringa = ''
    while indice >= 0:
        nuovaStringa += stringa[indice]
        indice -= 1
    print(nuovaStringa)


reverser(alfa)

print(list(alfa)) # converte la stringa alfa in una lista mettendo un carattere per ogni elemento della lista

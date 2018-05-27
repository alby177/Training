inventario = ['torcia', 'spada', 'pane elfico', 'arco']
print(inventario)

inventario.append('frecce') # permette di inserire un elemento alla fine della lista
print(inventario)

def riempiInventario():
    inventario = []
    while True:
        oggetto = input("Cosa vuoi aggiungere all'inventario?\n")
        if oggetto == 'terminato' or oggetto == 'Terminato':
            break
        else:
            inventario.append(oggetto)
            
    print('La lista prodotta è: ', inventario)


inventario.remove('spada') # permette di togliere l'elemento indicato come agomento della funzione
print(inventario)

inventario.sort() # ordina in ordine alfabetico la lista           
print(inventario)

numeri = [4, 5, 1, 12, -1, 3]
numeri.sort() # mette in ordine i numeri in ordine crescente
print(numeri)

# aggiungendo "Reverse" come parametro della funzione sort() ordina la lista in ordine inverso

print(inventario.index('frecce')) # permette di capire qual'è l'indice dell'elemento fornito come parametro

inventario.insert(2, 'canna da pesca') #inserisce alla posizione passata come parametro l'elemento passato come parametro
print(inventario)

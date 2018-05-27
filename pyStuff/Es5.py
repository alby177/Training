def divisore(a, b):
    try:
        risultato = a / b
        print('Il risultato della divisione è: ', risultato)
    except ZeroDivisionError: #nel caso di una divisione per zero l'errore viene gestito così in modo comprensibile
        print('Hai effettuato una divisione per 0')

divisore(12 , 2)
divisore(5, 0)

def moltiplicatore():
    
    try:
        a = int(input('Inserisci il valore del primo numero: '))
        b = int(input('Inserisci il valore del secondo numero: '))
        print(a * b)
        
    except ValueError:
        print('Solo caratteri numerici, riparte l\'esecuzione del programma')

    finally: # codice eseguito qualsiasi cosa succeda alla fine del programma
        print('Grazie per aver usato questa applicazione')

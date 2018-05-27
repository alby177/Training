while True:
    print('''
Benvenuto, qui trovi una semplice calcolatrice!
Creata da: Alberto
Di seguito un elnco delle varie funzioni disponibili

- Per effettuare un\'addizione seleziona 1;
- Per una sottrazione seleziona 2;
- Per effettuare una moltiplicazione seleziona 3;
- Per effettuare una divisione seleziona 4;
- Per effettuare un calolo esponenziale seleziona 5;
- Per uscire dal programma digitare ESC;
    ''')
    scelta = input('Inserisci il numero corrispondente all\'azione desiderata ----> ')

    if scelta == '1':
        print('\nHai scelto addizione\n')
        a = float(input('Inserisci il primo numero -> '))
        b = float(input('Inserisci il secondo numero -> '))
        print('Il risultato della somma è: ' + str(a + b))
        
    elif scelta == '2':
        print('\nHai scelto sottrazione\n')
        a = float(input('Inserisci il primo numero -> '))
        b = float(input('Inserisci il secondo numero -> '))
        print('Il risultato della sottrazione è: ' + str(a - b))

    elif scelta == '3':
        print('\nHai scelto moltiplicazione\n')
        a = float(input('Inserisci il primo numero -> '))
        b = float(input('Inserisci il secondo numero -> '))
        print('Il risultato della moltiplicazione è: ' + str(a * b))

    elif scelta == '4':
        print('\nHai scelto divisione\n')
        a = float(input('Inserisci il dividendo -> '))
        b = float(input('Inserisci il divisore -> '))
        print('Il risultato della divisione è: ' + str(a / b))

    elif scelta == '5':
        print('\nHai scelto sottrazione\n')
        a = float(input('Inserisci la base -> '))
        b = float(input('Inserisci l\'esponente -> '))
        print(' Il risultato della potenza è: ' + str(a ** b))

    elif scelta == 'ESC':
        print('Sto chiudendo l\'applicazione....')
        break

    else:
        print('Bad input command')

    loop = input('Desideri proseguire? S per continuare, N per uscire -> ')
    print('\n********************************************************')
    if loop == "S" or loop == "s":
        continue
    elif loop == "N" or loop == "n":
        break
    else:
        print('Invalid command')
        continue

    

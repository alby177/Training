#Programme per scrivere 10 numeri casuali tra 1 e 50
import random # importa una libreria
from math import sqrt #importa solo una funzione di una libreria

for numero in range (11):
    valore = random.randint(1, 50)
    print('The number is: ' + str(valore))
    print('The square root of the numbers is: ' + str(sqrt(valore)))


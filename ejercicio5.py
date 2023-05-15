# Determinar si una cadena de caracteres es un palindromo.

from stack import Stack

pila = Stack()
pila_aux = Stack()
pila_aux2 = Stack()
palabra = 'neuquen'


for caracter in palabra:
    pila.push(caracter)

while pila.size() > 0:
    dato = pila.pop()
    pila_aux.push(dato)
    pila_aux2.push(dato)

while pila_aux2.size() > 0:
    pila.push(pila.pop())

if pila.size() == pila_aux.size():
    palindromo = False
    while pila.size() > 0:
        if pila.pop() != pila_aux.pop():
            palindromo = True
            break

    print(palindromo)
else:
    print(False)




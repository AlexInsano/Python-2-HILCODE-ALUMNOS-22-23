import palabra
import verdad

palabra = palabra.palabras[0]
print(palabra)

letras = ""
letras, letra = verdad.funcionamiento(letras)
print("Letras",letras)
print("Letra",letra)

if letra in palabra():
    print("esta en la palabra")
    tam = len(palabra)
    for i in range(0,tam):
        in palabra[i] == letra:
            print("la letra",letra"is on position"i)

else:
    print("no esta en la palabra")

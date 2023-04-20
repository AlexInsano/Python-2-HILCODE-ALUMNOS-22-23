nombre_fichero = "fichero_palabras.txt"

def leer_fichero(nombre_fichero):
    palabras= []
    with open(nombre_fichero, "r") as f:
        for linea in f:
            palabra.replace("\n","")
            palabras.append(palabra)
    f.close()
    return palabras
palabras = leer_fichero(nombre_fichero)
print(palabras)
string ="asd d ddd ddd d"
cambio = atring.replace("d", "")
print(cambio)

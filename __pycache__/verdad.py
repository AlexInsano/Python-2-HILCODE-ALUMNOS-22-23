def funcionamiento(letras):
        letra=input("pon una letra :D" )
        while letra.upper() in letras:
            letra=input("pon una letra QUE NO SEA ESA :D" )
            letra = letra[0].upper()
            letras = letras + letra + " "
        return letras, letra

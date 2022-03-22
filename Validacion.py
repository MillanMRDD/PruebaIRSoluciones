
'Al final he encontrado una forma distinta a la que me mandste tu.'

class Validacion:

    print("Escriba su nombre:")
    nombre = input()
    print("Escriba su edad")
    edad = int(input())
    print("Escriba su nif")
    numDni = int(input())

    if edad >= 18:
        letraDni = None
        if numDni % 23 == 3:
            letraDni = "A"
        if numDni % 23 == 11:
            letraDni = "B"
        if numDni % 23 == 20:
            letraDni = "C"
        if numDni % 23 == 9:
            letraDni = "D"
        if numDni % 23 == 22:
            letraDni = "E"
        if numDni % 23 == 7:
            letraDni = "S"
        if numDni % 23 == 4:
            letraDni = "O"
        if numDni % 23 == 18:
            letraDni = "H"
        if numDni % 23 == 13:
            letraDni = "J"
        if numDni % 23 == 21:
            letraDni = "K"
        if numDni % 23 == 19:
            letraDni = "L"
        if numDni % 23 == 5:
            letraDni = "M"
        if numDni % 23 == 12:
            letraDni = "N"
        if numDni % 23 == 8:
            letraDni = "P"
        if numDni % 23 == 16:
            letraDni = "O"
        if numDni % 23 == 1:
            letraDni = "R"
        if numDni % 23 == 15:
            letraDni = "S"
        if numDni % 23 == 0:
            letraDni = "T"
        if numDni % 23 == 17:
            letraDni = "V"
        if numDni % 23 == 2:
            letraDni = "W"
        if numDni % 23 == 10:
            letraDni = "X"
        if numDni % 23 == 6:
            letraDni = "Y"
        if numDni % 23 == 14:
            letraDni = "Z"

        may = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        password = ""
        movimiento = 3
        
        for letra in nombre.upper():
            if letra in may:
                indice = may.find(letra)
                indice += movimiento
                if indice >= 27:
                    indice -= 27
                password += may[indice]
            else:
                password += letra

        print("La contraseña obtenida por el usuario con dni " +
              str(numDni) + letraDni + " es " + password)

    else:
        print("Es menor de edad")

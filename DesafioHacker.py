""" Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */"""

texto= (input("Escriba texto para codificar en lenguaje hacker: "))
mayus=texto.upper()
lista= list(mayus)

for letra in range(len(lista)):
    if lista[letra] == "A":
        lista[letra] = "4"
    if lista[letra] == "B":
        lista[letra] = "I3"
    if lista[letra] == "C":
        lista[letra] = "["
    if lista[letra] == "D":
        lista[letra] = ")"
    if lista[letra] == "E":
        lista[letra] = "3"
    if lista[letra] == "F":
        lista[letra] = "|="
    if lista[letra] == "F":
        lista[letra] = "|="
    if lista[letra] == "G":
        lista[letra] = "&"
    if lista[letra] == "H":
        lista[letra] = "#"
    if lista[letra] == "I":
        lista[letra] = "1"
    if lista[letra] == "J":
        lista[letra] = ",_|"
    if lista[letra] == "K":
        lista[letra] = ">|"
    if lista[letra] == "L":
        lista[letra] = "1"
    if lista[letra] == "M":
        lista[letra] = "/\/\\"
    if lista[letra] == "N":
        lista[letra] = "^/"
    if lista[letra] == "O":
        lista[letra] = "0"
    if lista[letra] == "P":
        lista[letra] = "|*"
    if lista[letra] == "Q":
        lista[letra] = "(_,)"
    if lista[letra] == "R":
        lista[letra] = "I2"
    if lista[letra] == "S":
        lista[letra] = "5"
    if lista[letra] == "T":
        lista[letra] = "7"
    if lista[letra] == "U":
        lista[letra] = "(_)"
    if lista[letra] == "V":
        lista[letra] = "\/"
    if lista[letra] == "W":
        lista[letra] = "\/\/"
    if lista[letra] == "X":
        lista[letra] = "><"
    if lista[letra] == "Y":
        lista[letra] = "j"
    if lista[letra] == "Z":
        lista[letra] = "2"
    

    
    
    





    
    

unir= "".join(lista)
print(unir)
        

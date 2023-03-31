def ParImpar():
    print("Bienvenido a nuestro programa para resolver si un número es par o impar")
    numero= int(input("¿En que número estás pensando?: "))

    while numero>1 and numero<1000 :
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")

        numero=int(input("Ingresa otro número"))
        continue
    else:
        print("el número ingresado es incorrecto")
        
            

    

    #todavia no funciona

ParImpar()
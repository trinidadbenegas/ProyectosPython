def esAnagrama (first_word, second_word):
    #ponemos las palabras en minúsculas
    first_word_lc= first_word.lower()
    second_word_lc= second_word.lower()
    
    #convertimos cadenas a listas
    listone= list(first_word_lc)
    listtwo =list(second_word_lc)

    #ordenamos las listas alfabeticamente
    listone.sort()
    listtwo.sort()
    #convertir a string de nuevo
   
    nuevaPalabra1= "".join(listone)
    nuevaPalabra2= "".join(listtwo)

    return nuevaPalabra1 == nuevaPalabra2

palabra1= input("Ingrese una palabra: ")
palabra2= input("Ingrese otra palabra: ")


print(esAnagrama(palabra1, palabra2))  


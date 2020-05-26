print "Ejercicios 1.1.2"
print "\nEscriba una función llamanda display_message() que imprima en la pantalla un mensaje que indique los temas que se han visto hasta el momento."
def display_message():
    print "\nLos temas vistos hasta el momento son:"
    print "Funciones"
    print "Clases"
display_message()


print "\nEscriba una función que se llame libro_favorito() que acepte un parámetro llamado titulo y que despligue en la terminal *Tu libro favorito es (nombre del libro)*"
def libro_favorito(titulo):
    print ("Tu libro favorito es: " + titulo.title())
libro_favorito(raw_input('titulo de tu libro favorito: '))


print("\nEscriba una función llamanda hacerPlayera() que acepte como argumento, el tamaño y un texto que apararecerá cerigrafeado en la playera. La función deberá imprimir en la terminal algo parecido a lo siguiente")
def hacerPlayera(texto, tamano):    
    print ("\nLa playera es talla "+tamano+ " y el texto a grafitear es: "+texto)
    
tallas=['Chica','Mediana','Grande','Extra grande']
l=input("\nEliga un numero para una talla \n0 para la chica \n1 para la mediana \n2 para la grande \n3 para la extra grande \nTalla= ")
tamano=tallas[l]
texto=raw_input("\nponga lo que se vaya a grafitear en la playera ")
hacerPlayera(texto,tamano)

def hacerPlayera(texto='yo <3 Python',tamano='Grande'):
    print ("\nLa playera es talla "+tamano+ " y el texto a grafitear es: "+texto)
hacerPlayera()
hacerPlayera(tamano="mediano")
hacerPlayera(texto="hola bbe",tamano="chica")

print "\nEscriba una función llamada descripcionCiudad() que acepte como argumentos el nombre de una ciudad y el nombre de un país como argumentos y que imprima en la terminal un texto como: Xalapa está en México, Río de Janeiro está en Brazil, París está en Fracia. Ponga como valor predeterminado *México* a la variable país, y llame a la función tres veces donde por lo menos una ciudad no pertenezca al país México."
def descripcionciudad(ciudad,pais='Mexico'):
    print ("\nla ciudad "+ ciudad.title()+" esta en "+pais)
descripcionciudad(ciudad="Estado de mexico")
descripcionciudad(ciudad="Polonia",pais="Alemania")
descripcionciudad(ciudad="Baja california")


print"\nHacer un módulo con las funciones básicas para una calculadora, suma, resta, producto y división, en la función de división si el denomidador es igual a cero debe de volver a leer el valor del denominador hasta que sea distinto de cero (se recomienda utilizar el ciclo while y el condicional if)"
print "\nCalculadora"
calcu=['tte','suma','resta','multiplicacion','division','salir']
print "Menu \n1 Suma \n2 Resta \n3 Multiplicacion \n4 Division \n5 Salir"
def calculadora():
    opc= int(input("Seleccione una opcion "))
    while (opc >0 and opc <5):
        num1= int (input("ingrese un numero "))
        num2=int(input("ingrese un numero "))
        if(opc==1):
            print "la suma es: ", num1+num2
            opc=int (input("seleccione una opcion "))
        elif (opc==2):
            print "la resta es: ", num1-num2
            opc=int (input("seleccione una opcion "))
        elif (opc==3):
            print "la multiplicacion es: ", num1*num2
            opc=int (input("seleccione una opcion "))
        elif (opc==4):
            try:
                print"la division es: ",num1/num2
                opc=int(input("seleccione una opcion "))
            except ZeroDivisionError:
                print("no se puede dividir entre cero")
                opc=int(input("seleccione una opcion "))

calculadora()
    
print"\nHacer una función que el usuario introduzca un número y la función debe de desplegar un triángulo de sumas, Como ejemplo, si el usuario manda a la función 4 debeía imprimir el siguiente arreglo"
print("\nIngrese el numero de filas para la piramide")
num = input()
for i in range(num):
    print(' ' * (num - i - 1) + "*" * (1 * i + 1))

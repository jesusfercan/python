"""
Los operadores son utilizados para realizar operarciones matematicas
+ - / * % etc

operador // es una division pero te devuelve un numero entero redondeado
operador ** es para realizar un exponente (x elevado a)

El operador + tambien sirve para concatenar cadenas
"""
print("")

print("Hola " + "World")

print("")
print("Hola " + str(10))

print("")
print("Hola " * 5) # Si se incluye el operador de multiplicacion, te muestra X veces ese texto (solo permite valores enteros)


"""
Operadores comparativos
> < == != <= >=
"""
print(1<=4)
print(4>=1)
print(4==4)
print(1!=4)
print(4<4)
print(4>4)


# Tambien se pueden comparar cadenas de caracteres (lo que compara es la ordenacion alfabetica)
# para comparar el tamaño del string, se utiliza la funcion len()
print("")
print("Hola" > "Hola")
print("A" < "B")
print("A" == "B")

"""
OPERADORES LOGICOS
or
and
not -> realiza la negación de un valor booleano
"""
print("")
print(True or False)
print(True and False)
print(not False)
print(True and (not False))
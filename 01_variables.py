# Variables
'''
- no se define el tipo de variable, esto va intrinseco
- las variables en python se definen siempre en minusculas y para separar palabras se recomienda usar el barra baja _
- cuando el nombre de la variable es una palabra reservada Ej: if, se define con barra baja: _if
'''

print('')
mi_variable_string = "Variable tipo string"
print("Valor mi_variable_string: " ,mi_variable_string)

print('')
variable_int = 1
print("Valor variable_int: " , variable_int) 
print(type(variable_int))

print('')
variable_int_en_str = str(variable_int)
print("Valor variable_int en String: " , variable_int_en_str) 
print(type(variable_int_en_str))

print('')
variable_float = 1.1
print("Valor variable_float: " , variable_float)
print(type(variable_float))
print("Valor suma int y float: " , variable_int + variable_float)


print('')
variable_boolean = True
print("Valor variable_boolean: " , variable_boolean)
print(type(variable_boolean))


print('')
print('Concatenacion de las variables')
# concatenacion de variables se hace con , en el print y la coma ya incluye un espacio en blanco de separacion
print(mi_variable_string, '/', 
      variable_int, '/',
      variable_int_en_str, '/',
      variable_float)

print('')
print("Funcion len tamaño para mi_variable_string" , len(mi_variable_string))
print("Funcion len tamaño para variable_int" , len(variable_int_en_str))


# declaracion de variables en una sola linea
nombre, apellidos, alias, edad = "jesus", "fernandez", "jesusfercan", 34
print("Me llamo" , nombre, apellidos, ", con alias:", alias, "y edad: ", edad )



# funcion inputs para entra entrada de datos
nombre_input = input('Cual es tu nombre?')
print("Encantado",nombre_input,"!")


'''
las variables pueden cambiar sus tipos en ejecucion, ya que no se definen en si
nombre antes era string y ahora lo cambiamos a entero
'''
print("tipos de nombre y edad antes de cambiarlos")
print(type(nombre), type(edad))
nombre = edad
edad = apellidos
print("tipos de nombre y edad antes de cambiarlos")
print(type(nombre), type(edad))
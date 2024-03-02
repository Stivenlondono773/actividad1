#variables, if, elif

nombre = str ( input("digie su nombre "))
apellido = str (input ("digite sus apellidos "))
edad = int (input(" digite su edad "))


if edad <= 16 :
  print("hola pequeño ", nombre , apellido)

elif edad >= 17 and edad <= 20 :
  print( "hola adolecente ", nombre, apellido)

elif edad > 20 :
  print("hola Señ@r ", nombre,apellido)

else: 
  (" hola " ,nombre, apellido)

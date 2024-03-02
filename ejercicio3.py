#wile 

estudiantes = 0
nombre_estudiante = str(input("ingrese su nombre completo "))
edad_estudiante = int (input("ingrese su edad"))



while estudiantes < 3:
    print("hola ", nombre_estudiante, "su edad es ", edad_estudiante, "su registro es el numero", estudiantes + 1 ) 
    estudiantes += 1 

print("bienvenido ",nombre_estudiante, "con el registro numero", estudiantes)

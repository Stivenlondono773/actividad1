"""""En la empresa donde trabajo calculamos la cantidad de MFC(GLIOXAL) que se le agrega a un tanque
teniendo encuenta que su capacidad maxima es de 1000 litros, para esos 1000 litros se necesitan
una camtidad determinada de  MFC(GLIOXAL). el requerimiento es hacer una app que calcule la cantidad de mfc, dependiendo 
de la cantidad de litros del tanque, teniendo encuenta que la cantidad de mfc la dan en kilos. la dencidad del MFC es de 1.272"""""


cantidadlitros = float (input("digite la cantidad de litros a preparar en el tanque "))
cantidadmfc_kg = float (input("digite la cantidad de kilos de mfc para mil litros de alcohol "))
dencidadmfc = 1.272
tanque = 1000


cantidadmfc_litros = cantidadmfc_kg/dencidadmfc





total_mfc_al_tanque = cantidadlitros * cantidadmfc_litros / 1000

print("la cantidad de mfc para ", cantidadlitros ,"litros de alcohol es ", total_mfc_al_tanque ,"litros de mfc")




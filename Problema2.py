nom = input ("Ingrese su nombre:")
ruc = input ("Ingrese su numero de ruc:")
if len (ruc)>11:
    print ("El numero de ruc es mayor que 11")
elif len(ruc)<11:
    print ("El numero de ruc es menor que 11")
else : 
 print ("Los datos se han ingresado correctamente")
 print ("---------RESULTADO----------")
 print (nom)
 print (ruc)

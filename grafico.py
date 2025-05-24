valor_dolar = float(input("el valor del dolar es: "))
pesos = float (input("Ingrese la cantidad de pesos: "))
dolares = pesos/ valor_dolar
dolares = f"{dolares:.2f}"
print ("usted tiene " , dolares , "UD$")
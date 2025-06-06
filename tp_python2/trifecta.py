programa = True
# Bucle principal: se repite hasta que el usuario decida salir con 0.
while programa:
    nombre = input("Ingrese su nombre ")
    print(f"Hola {nombre} Bienvenido/a al programa!:")


    valido = False  # Bandera: True si la entrada inicial es un entero válido.
    inicio = 0      # Almacena el número entero ingresado para iniciar/salir.

    # Bucle interno: asegura que la primera entrada sea un número entero.
    while not valido:
        entrada = input("Por favor, ingrese un número entero o ingrese 0 para finalizar el programa: ")

        ok_check = False # Bandera temporal para la validación de la 'entrada' actual.
        if entrada:      # Verifica que la 'entrada' no esté vacía.
            if entrada[0] == '-': # Comprueba si es un posible número negativo.
                if len(entrada) > 1 and entrada[1:].isdigit(): # Valida si el resto son dígitos.
                    ok_check = True
            elif entrada.isdigit(): # Valida si toda la 'entrada' son dígitos (positivo/cero).
                ok_check = True

        if ok_check: # Si 'entrada' es un entero válido...
            inicio = int(entrada) # Convierte el texto a número entero.
            valido = True         # Permite salir del bucle de validación.
        else:
            print(f"\n Lo siento {nombre}, no ingresaste un cacarter valido. El programa ha finalizado. \n")
            print(f" Hasta pronto {nombre} ")
            programa = False
            break
    if not programa:
      continue

    # Verifica si el usuario quiere salir del programa.
    if inicio == 0:
        print(f"Ha ingresado 0. Finalizando el programa. Hasta pronto {nombre}")
        break # Sale del bucle principal.

    else:
        print(f"Número de inicio ingresado: {inicio}. ¡El programa continúa!")

        frase = input("Ahora, ingrese una palabra o frase: ") # Recoge la frase del usuario.
        largo_frase = len(frase) # Cuenta la cantidad de caracteres de la frase.
        print(f"Tu frase o palabra contiene {largo_frase} caracteres.")

        # Calcula el factorial de 'largo_frase'.
        if largo_frase == 0:
            factorial = 1 # Factorial de 0 es 1.
        else:
            factorial = 1 # Acumulador para el cálculo del factorial.
            i = 1    # Contador para el bucle del factorial.
            while i <= largo_frase:
                factorial *= i
                i += 1

        # Muestra el factorial y verifica si es par o impar.
        print(f"El factorial de {largo_frase} es: {factorial}")

        if largo_frase == 0 or largo_frase == 1:
            print("El número factorial resultante es IMPAR.")
        else:
            print("El número factorial resultante es PAR.")

        print(f"\n--- ¡Felicitaciones {nombre}! Completaste el programa! Hasta pronto! ---\n")
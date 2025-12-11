import os
salir = 'no'
while(salir == 'no'):
    os.system('clear')
    # Entrada
    print(' ======= CALCULADORA CON PYTHON ============')

    print('=========== OPCIONES =============')
    print('1: Suma')
    print('2: Resta')
    print('3: Multiplicacion')
    print('4: Divison')
    print('5: Tabla de multiplicar')

    opcion = int(input('Ingrese la opcion que desea: '))

    if opcion == 5:
        tabla = int(input('Ingrese la tabla de multiplicar que desea ver: '))
        for contador in range(1,13,1):
            resultado = tabla * contador
            print(f'{tabla} x {contador} = {resultado}')
    elif(opcion >= 1 and opcion <= 5):
        numero1 = int(input('Num1: '))
        numero2 = int(input('Num2: '))
    
        if opcion== 1:
            operacion = 'suma'
            resultado = numero1 + numero2
        elif opcion == 2:
            operacion = 'resta'
            resultado = numero1 - numero2
        elif opcion == 3:
            operacion = 'multiplicacion'
            resultado = numero1 * numero2
        elif opcion == 4:
            operacion = 'division'
            resultado = numero1 / numero2
        else:
            print('Operacion invalida')
            exit()
# SALIDA
        print( f'La {operacion} de {numero1} y {numero2} es {resultado}')

    salir = input('Desea salir? (si/no): ')
    if salir =='si':
        break
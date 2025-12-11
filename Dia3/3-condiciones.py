# CALCULADORA

# ENTRADA
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
operacion = input('Ingrese la operacion a realizar(+,-,*,/): ')

# PROCESO
if operacion == '+':
    resultado = numero1 + numero2
elif operacion == '-':
    resultado = numero1 - numero2
elif operacion == '*':
    resultado = numero1 * numero2
elif operacion == '/':
    resultado = numero1 / numero2
else:
    print('Operacion invalida')
    exit()
# SALIDA
print( f'{numero1} {operacion} {numero2} = {resultado}')
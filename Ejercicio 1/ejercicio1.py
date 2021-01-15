def isInt():
    while True:
        num = input('Escribe un numero entero entre 1 y 10: ')
        try:
            num = int(num)
            if num < 1 or num > 10:
                print('Valor fuera de rango: escribe un valor entre 1 y 10')
            else:
                return num
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")


n = isInt()
m = isInt()

file = 'tabla-' + str(n) + '.txt'
try:
    f = open(file, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])

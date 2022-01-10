import math

a = eval(input("Digite um número "))
b = eval(input("Digite um número "))
c = eval(input("Digite um número "))

delta = b ** 2 -4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
else:
    if delta == 0:
        raiz1 = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        print('a raiz desta equação é', raiz1)
    else:
     raiz1 = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
     raiz2 = ((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
     if raiz2<raiz1:
        print("as raízes da equação são", raiz2, "e",raiz1)
     else:
        print("as raízes da equação são", raiz1, "e", raiz2)

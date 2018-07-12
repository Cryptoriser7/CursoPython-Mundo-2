"""Refaça o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo ser´formado

-Equilátero: todos os lados iguais
-Isósceles: Dois lados iguais
-Escaleno: todos os angulos diferentes"""


a = float(input('comprimento 1: '))
b = float(input('Comprimento 2: '))
c = float(input('Comprimento 3: '))
print()

if b - c < a < b + c and a - c < b < a + b and a - b < c < a + b:
    print('Pode-se formar um triangulo')
    if b == a and b == c:
        print('Pode-se format um triangulo Equilátero')

    elif b == c or a == c or b == a:
        print('Pode-se formar um tringulo Isósceles')

    else:
        print('Pode-se formar um triangulo Escaleno')

else:
    print('Não se pode formar um triangulo')


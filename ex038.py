'''Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior; O segundo valor é maior; nao existe valor maior, os dois sao iguais.
'''

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))

if n1 < n2:
    print('O segundo valor é maior')
elif n2 < n1:
    print('O primeiro valor é maior')
elif n1 == n2:
    print('Os números são iguais')

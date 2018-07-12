#Desenvolva uma lógia e o peso e altura de uma pessoa, calcule seu IMC e mostre eu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo de Peso
#-Entre 18.5 e 25: Peso ideal
#-25 até 30: Sobrepeso
#-30 até 40: Obsidade
#-Acima de 40: Obsidade morbida


peso = float(input('Peso em quilogramas: '))
altura = float(input('Altura em metros: '))
imc = peso / (altura * altura)


print()

print('IMC: {:.2f}'.format(imc))

print()
if imc <= 18.4:
    print('Abaixo de Peso')
elif 18.5 <= imc <= 24.9:
    print('Peso Ideal')
elif 25 <= imc <= 29.9:
    print('Sobre Peso')
elif 30.0 <= imc <= 39.9:
    print('Obesidade')
elif imc >= 40.0:
    print('Obesidade Morbida')

"""Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com a sua idade:

-Se ele ainda vai ter que se alistar no serviço
-Se é a hora de se alistar
-Se já passou do tempo de alistamento

O programa também deverá mostrar o tempo que falta para se alistar ou que passou do prazo!"""


import time
year = time.localtime().tm_year
year_youth = int(input('Ano de nascimento do recruta: '))
age = year - year_youth
print()

if age == 18:
    print('Parabéns recruta, você tem 18 anos e está na hora de se alistar!! ')
elif age <= 18:
    print('Infelizmente voce ainda nao se pode alistar! Aguarde mais {} ano(s)'.format(18 - age))
elif age >= 18:
    print('Onde andou você no(s) ultimo(s) {} ano(s)!?? Voce esta ATRASADO, Moleque!!!!'.format(age - 18))




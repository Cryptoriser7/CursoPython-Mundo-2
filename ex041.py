'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade

-Até 9 anos: MIRIM
-até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SÉNIOR
-Acima: MASTER'''
import time
year = time.localtime().tm_year
date = int(input('ANO NASCIMENTO: '))
age = year - date

if age <= 9:
    print('O Atleta tem {} anos, portanto corresponte á classe MIRIM'.format(age))
elif 9 <= age <=14:
    print('O Atleta tem {} anos, portanto corresponde á classe INFANTIL'.format(age))
elif 14 <= age <= 19:
    print('O atleta tem {} anos, portanto corresponde á classe JUNIOR'.format(age))
elif 19 <= age <= 20:
    print('O atleta tem {} anos, portanto corresponde á classe SÉNIOR'.format(age))
elif age >=20:
    print('O atleta tem {} anos, portanto corresponde á classe MASTER'.format(age))

'''Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagen no final, de acordo com a media atinifa

-Media abaixo de 5.0: REPROVADO
-Media entre 5.0 e 6.9: RECUPERAÇÂO
-Média 7.0 ou superior: APROVADO'''

notaum = float(input('Nota 1: '))
notadois = float(input('Nota 2: '))
media = (notaum + notadois) / 2

print('Média: {:.1f}'.format(media))

if media <= 4.9:
    print('Nota inferior a 5.0. REPROVADO')
elif 5.0 <= media <= 6.9:
    print('Nota compreendida entre 5 e 7. RECUPERAÇÂO')
elif media >= 7.0:
    print('Nota superior a 7.0. APROVADO!!')

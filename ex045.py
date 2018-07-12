'''Crie um programa que faça o computador jogar jokenpô (pedra, papel, tesoura) com voce'''

print('            \033[34m<<\033[31mJO\033[33mKEN\033[32mPÔ\033[34m>>\033[0m')
#Importação de random.choice, para ser usado na automação da escolha do computador
#Recebe input numerico do user que mais tarde é convertido para a palavra equivalente
from random import choice
lista = ['Pedra', 'Papel', 'Tesoura']
user_choice = int(input('Pedra (1), Papel (2) Ou Tesoura (3)?\n==> '))
pc_choice = choice(lista)

#Tradução do user input
if user_choice == 1:
    user_choice_trasl = 'Pedra'
elif user_choice == 2:
    user_choice_trasl = 'Papel'
elif user_choice == 3:
    user_choice_trasl = 'Tesoura'
else:
    user_choice_trasl = 'Ahn?!'
    print('Nao percebemos o que fizeste com a tua mao!? Repete novamente!\n(input nao reconhecido)')

#Motor do jogo (simples)
if user_choice <= 3:
    print('\033[31mPC\033[0m ==> (\033[34m{}\033[0m  vs  \033[34m{}\033[0m) <== \033[32mVOCÊ\033[0m'.format(pc_choice, user_choice_trasl))
    #condiçoes de vitoria
    if pc_choice == 'Pedra' and user_choice_trasl == 'Pedra':
        print('\033[33mEMPATE\033[0m!!')
    elif pc_choice == 'Pedra' and user_choice_trasl == 'Tesura':
        print('\033[31mPC GANHOU\033[0m!!')
    elif pc_choice == 'Pedra' and user_choice_trasl == 'Papel':
        print('\033[32mVOCÊ GANHOU\033[0m!!')
    elif pc_choice == 'Papel' and user_choice_trasl == 'Tesoura':
        print('\033[32mVOCÊ GANHOU\033[0m!!')
    elif pc_choice == 'Papel' and user_choice_trasl == 'Papel':
        print('\033[33mEMPATE\033[0m!!')
    elif pc_choice == 'Papel' and user_choice_trasl == 'Pedra':
        print('\033[31mPC GANHOU\033[0m!!')
    elif pc_choice == 'Tesoura' and user_choice_trasl == 'Pedra':
        print('\033[32mVOCÊ GANHOU\033[0m!!')
    elif pc_choice == 'Tesoura' and user_choice_trasl == 'Papel':
        print('\033[31mPC GANHOU\033[0m!!!!')
    elif pc_choice == 'Tesoura' and user_choice_trasl == 'Tesoura':
        print('\033[33mEMPATE\033[0m!!')
    else:
        print('Erro qualquer. Isto nao devia aparecer')

elif user_choice >= 3:
    print()








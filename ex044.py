'''elabora um programa que calcula o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

-Á vista dinheiro/cheque: 10% de desconto
-Á vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% juros'''

print()
print('Formuladora de Pagamentos MGate')
print('.' * 20)
print('Powered by Python')
print('.' * 20)
print()
print('Diferentes metodos de pagamento\n1-Dinheiro\n2-Cartão\n3-2x Cartão\n4-3x ou mais Cartão')
print('.' * 20)
print()
print('Por Favor introduza o valor da compra em Euros:')
print()
valor = float(input('€: '))
print()
print('Agora selecione um dos métodos de pagamento de 1 a 4')
metodo = int(input('Método: '))



if metodo == 1:
    print('Selecionou pagamento em dinheiro')
    conf1 = str(input('Concorda? (S ou N): ')).capitalize().strip()
    if conf1 == 'S':
        print('Pagamento final com 10% desconto ativo: \033[36m{:.2f}\033[0m €'.format(valor * 0.90))
    elif conf1 == 'N':
        print('Voce não concordou com o metodo de pagamento. Fechando')
    else:
        print('Resposta não reconhecida. Fechando')
        
elif metodo == 2:
    print('Selecionou pagamento em Cartão')
    conf2 = str(input('Concorda? (S ou N): ')).capitalize().strip()
    if conf2 == 'S':
        print('Pagamento final com desconto de 5% ativo: \033[36m{:.2f}\033[0m €'.format(valor * 0.95))
    elif conf2 == 'N':
        print('Voce não concordou com o metodo de pagamento. Fechando')
    else:
        print('Resposta não reconhecida. Fechando')

elif metodo == 3:
    print('Selecionou pagamento em 2x no Cartão')
    conf3 = str(input('Concorda? (S ou N)')).capitalize().strip()
    if conf3 == 'S':
        print('Pagamento final 0% taxas de juro: \033[36m2x {:.2f}\033[0m €'.format(valor / 2))
    elif conf3 == 'N':
        print('Voce não concordou com o metodo de pagamento. Fechando')
    else:
        print('Resposta não reconhecida! Fechando!')

elif metodo == 4:
    print('Selecionou pagamento em 3x ou mais no Cartão com 20% juros')
    conf4 = str(input('Concorda? (S ou N)')).capitalize().strip()
    if conf4 == 'S':
        x = int(input('Número de Vezes: '))
        print('Pagamento final com 20% juros,{}x no Cartão no valor de \033[36m{}x {:.2f}\033[0m €'.format(x, x, (valor * 1.20) / x))
    elif conf4 == 'N':
        print('Voce não concordou com pagamento. Fechando')
    else:
        print('Resposta não reconhecida. Fechando')

else:
    print('Metodo não identificado, por favor tente novamente de 1 a 4')
print()
print('Obrigado por usar softwares MGate')



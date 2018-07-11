'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#O programa vai perguntar o Valor da casa, o Salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal sabendo que ela nao pode exceder 30% do salário ou entao o emprestimo será negado.
'''

ValorCasa = int(input('Valor do Imóvel: '))
Salario = int(input('Salário: '))
Anos = int(input('Duração Emprestio: '))
prestacao = ValorCasa / (Anos * 12)

print('O valor da sua prestação será: {:.2f} €'.format(prestacao))
print('.' * 20)
if (prestacao / Salario) * 100 <= 30.0:
    print('A prestação para o credito pedido representa {:.2f} % do seu salário'.format((prestacao / Salario) * 100))
    print('Como a percentagem é inferior a 30 %, o seu crédito será \033[36mAPROVADO\033[0m!')
elif (prestacao / Salario) * 100 >= 30.0:
    print('A prestação para o credito pedido representa {:.2f} % do seu salário'.format((prestacao / Salario) * 100))
    print('Como a percentagem é superior a 30 %, o seu credito será \033[33mREPROVADO\033[0m')



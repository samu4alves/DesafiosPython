br = ('-')
br2 = ('=')
print(br2 * 70)
# NOME DO PROGRAMA
print('CONVERSOR DE MOEDAS MX4')
print(br2 * 70)
# APRESENTAÇÃO USUÁRIO
print('SE APRESENTE, POR FAVOR !')
nome = input('Qual seu nome ?:')
# APRESENTAÇÃO PROGRAMA
print(f'\nOlá {nome}, tudo bem ?. Me chamo MX04')
# INSTRUÇÃO
print('Com valor do real, mostrarei quantas moedas se compra de outro país!')
print(br * 70)
# OPÇÃO PARA VER O SALDO ANTES DA CONVERSÃO
saldo = float(input('Deposite seus reais aqui, R$:'))
print(f'Antes da conversão, você está com R${saldo} reais de saldo')
# CALCULO DA CONVERSÃO
real = float(input('\nQuantos reais você quer converter ? R$:'))
dolar = real / 4.79
euro = real / 5.39
rbrusso = real / 0.053
print(br2 * 70)
print(f'Com R${real} reais, se compra ${dolar:.2f} dólares')
print(f'Com R${real} reais, se compra €{euro:.2f} euros')
print(f'Com R${real} reais, se compra ₽{rbrusso:.2f} rublos russos')
print(br2 * 70)
# OPÇÃO PARA VER O SALDO DEPOIS DA CINVERSÃO
saldo2 = saldo - real
print(f'Depois da conversão, seu saldo é de R${saldo2:.2f} reais')
# AGRADECIMENTOS AO USUÁRIO
print(f'{nome}, obrigado por usar o conversor. Um ótimo dia !')
print(br * 70)

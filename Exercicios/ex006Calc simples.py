# PEDIDO DE APRESENTAÇÃO, E SE APRESENTANDO
print('Para nos conhecermos !')
nome = input('Qual seu nome ?:')
print(f'\nOlá, {nome}. Tudo bem ? Me chamo MX04') 

print(f'''{'=' * 60}
{nome}. Um número, e mostrarei umas contas sobre ele !''')


base = int(input('Digite um número?:'))

dobro = base + base
triplo = base + base + base
raiz = base ** (1/2)

print(f'''\nO dobro de {base} é {dobro}
O triplo de {base} é {triplo}
A raiz de {base} é {raiz:.2f}''')

print(f'''{'-' * 60}
Obrigado por participar, {nome} !
{'=' * 60}''')

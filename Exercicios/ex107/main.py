import moeda

valor = float(input('Digite um preço: '))
print(f'''A metade {valor} é {moeda.metade(valor)}
O dobro de {valor} é {moeda.dobro(valor)}
Aumentando 10%, temos {moeda.aumentar(valor, 10)}
Reduzindo em 13%, temos {moeda.diminuir(valor, 13)}''')

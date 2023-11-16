# CONTADORES
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto:'))
    preço = float(input('Preço R$:'))
    resp = input('Quer continuar? [S/N]:').strip().upper()[0]
# PRODUTO TOTAL
    cont += 1
    total += preço
# PRODUTO MAIOR DE R$1000
    if preço > 1000:
        totmil += 1
# PRODUTO MAIS BARATO
    if cont == 1:
        barato = produto
        menor = preço
    else:
        if preço < menor:
            menor = preço
# FINAL E RESULTADO
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]:').strip().upper()[0]
    if resp == 'N':
        break
print(f'''=== FIM DO PROGRAMA ===
O total da compra foi {total:.2f}
{totmil} Produto custa acima de R$1000.00
O produto mais barato foi {barato} que custa R${menor:.2f}''')

br = ('=')
br2 = ('-')
print(br * 70)
# APRESENTAÇÃO DO NOME DO PROGRAMA
print('                 PAGAMENTO DOS CARROS ALUGADOS |MX4|')
print(br * 70)
# INFORMAÇÃO DO NOME PARA AGRADECIMENTOS NO FINAL
nome = input('Qual seu nome? Por favor!:'.upper())
# INFORMAÇÕES PARA O CALCULO DO ALUGUEL
dias = float(input('Quantos dias foi alugado?:'.upper()))
km = float(input('Quantos Km rodados?:'.upper()))
# INFORMAÇÕES DE ATRASO PARA MULTAS
print('\n   SE NÃO HOUVE ATRASO NA ENTREGA, DIGITE 0 !')
atraso = float(input('Houve atraso na entrega do veículo ?'.upper()))
total = (dias * 60) + (km * 0.15) + (atraso * 30)
print(br * 70)
# INFORMAÇÕES DO CAIXA E NOTA DOS VALORES
print('                        CAIXA')
print(br * 70)
print('\n                       NOTA')
print(f'DIAS = R${dias:.2f}')
print(br2 * 70)
print(f'KM = R${km:.2f}')
print(br2 * 70)
print(f'ATRASO = R${atraso:.2f}')
print(br2 * 70)
print(f'\nO total a pagar é de R${total:.2f} reais !'.upper())
print(br * 70)
# AGRADECIMENTOS
print(f'OBRIGADO PELO USO DOS NOSSO SERVIÇOS {nome}!'.upper())
print('A MX4, AGRADEÇE A CONFIANÇA.')
print(br * 70)

br = ('-')
br2 = ('=')
print(br2 * 70)
print('CONVERSOR DE ÁREA PARA QUANTIDADE DE TINTA')
print(br2 * 70)
print('\nVOU CALCULAR AS MEDIDAS FORNECIDAS')
print('E ENTÃO MOSTRAREI OS LITROS NECESSÁRIOS DE TINTA !')
print(br * 70)
print('INSTRUÇÃO: DIGITE SOMENTE NÚMEROS, PARA EVITAR ERROS !')
print(br2 * 70)
lgr = float(input('Qual a largura da parede?:'))
alt = float(input('Qual a altura da parede ?:'))
area = lgr * alt
print(f'A sua parede é {lgr} x {alt} logo a área total tem {area}m²')
paint = area / 2
print(br * 70)
print(f'\nPARA PINTAR A SUA PAREDE, PRECISARÁ DE {paint} litros de tinta !')
print(br2 * 70)
    
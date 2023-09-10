from time import sleep
# NOME DO PROGRAMA
print('=' * 70)
print('CONSULTA DE MULTAS')
print('=' * 70)
# INSTRUÇÕES
print('''DIGITE A SUA VELOCIDADE
E DESCUBRA SE LEVOU MULTA OU NÃO !
''')
# INFORMAÇÕES PARA O CÁLCULO
velocidade = float(input('Quantos km por hora:'))
print('CONSULTANDO...')
sleep(3)
# CÁLCULO
multa = (velocidade - 80) * 7
# USUÁRIO
if velocidade > 80:
    print('=' * 70)
    print(f'''\nMá notícia, essa velocidade é multa !
Isso vai custar R${multa:.2f} reais.

FIQUE ATENTO, ATÉ 80KM/H É PERMITIDO !
''')
    print('=' * 70)
else:
    print('=' * 70)
    print('''\nÓtima notícia !
essa velocidade não dá multa.

FIQUE ATENTO, ATÉ 80KM/H É PERMITIDO !
TENHA UM BOM DIA, E DIRIJA COM SEGURANÇA.
''')
    print('=' * 70)
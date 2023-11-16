# NOME DO SIMULADOR
print('=' * 50)
print('BANCO DEV')
print('=' * 50)
caixa = int(input('Qual valor você quer sacar? R$:'))
# LÓGICA
total = caixa
cedula = 100
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 0
        totced = 0
        if total == 0:
            break
print('TENHA UM BOM DIA ! | BANCO DEV, AGRADECE |')

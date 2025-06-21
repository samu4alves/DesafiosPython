numeros = []

while True:
    try:
        numero = int(input('Digite um número, a ser cadastrado: '))
        if numero in numeros:
            print(f'Número {numero} já existe !')
        else:
            numeros.append(numero)
            print(f'Número {numero}, cadastrado !')
        
        parada = input('Continua? (s/n): ').strip().lower()
        if parada == "s":
            continue        
        else:
            for num, nums in enumerate(numeros):
                numeros.sort()
                print(f'Valores cadastrados: {nums}')

    except Exception as e:
        print(f'Não foi possível executar a operação ! {e}')
    finally:
        continue
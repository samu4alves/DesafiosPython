numeros = []

while True:
    try:
        numero = int(input('Digite um número: '))
        numeros.append(numero)

        parada = input('Continua? (s/n): ').strip().lower()
        if parada == "s":
            continue
        else:
            cont = len(numeros)
            print(f'Foi digitado: {cont} números')
            
            num = enumerate(numeros)
            numeros.sort(reverse=True)
            print(f'Os valores decrescentes são {numeros}\n')
            
            if 5 in numeros:
                print('O valor 5 está na lista !')
            else:
                print('O valor 5 não está na lista')
    
    except Exception as e:
        print(f'Não foi possível executar a operação {e}')
    finally:
        continue
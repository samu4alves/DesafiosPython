from random import randint
from time import sleep

print(f'''{'-' * 50}
      JOGA NA MEGA SENA
{'-' * 50}''')

lista = list()
jogos = list()

quant = int(input('Quantos jogos para sorteiar: '))
total_jogos = 1

while total_jogos <= quant:
    contador = 0

    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1

        if contador >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogos += 1

print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

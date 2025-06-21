from random import randint
from time import sleep
# SORTEIO DE NÚMERO ( MAQUINA )
maquina = randint(0, 5)
# NOME DO JOGO
print('-=-' * 20)
print('JOGO DA ADVINHAÇÃO')
print('-=-' * 20)
# INSTRUÇÔES
print('Vou pensar em número entre 0 e 5, tente advinhar...')
print('_' * 60)
# USUÁRIO
jogador = int(input('Em que número eu pensei ?:'))
print('DEIXA EU VER...')
sleep(3)
if jogador == maquina:
    print('PARABÉNS ! Você conseguiu me vencer !')
else:
    print(f'GANHEI ! Eu pensei no número {maquina} e não no número {jogador}')

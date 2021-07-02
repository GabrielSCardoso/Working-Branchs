from random import randint

computador = randint(0, 10)
print('\033[1;31mSou seu computador... Acabei de pensar em um número entre 0 e 10.\033[m')
print('\033[1;31mSerá que você consegue adivinhar qual foi ?\033[m')

nome = str(input('Digite seu nome: '))
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print(f'{nome} Acertou! com {palpites} palpites. Parabéns')

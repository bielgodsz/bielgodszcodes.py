import random
from time import sleep
from emoji import emojize
cont = 0
print('=-='* 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='* 13)
while True:
    num_jogador = int(input('Digite um número: '))
    escolha = input('Par ou Ímpar? [P/I] ').upper()[0]
    print('-'* 40)
    computador = random.randint(0, 10)
    cont += 1
    print(emojize('Você tá pronto? :smiling_imp:', language='alias'))
    for i in range(3, 0, -1):
        print(i)
        sleep(2)
    if escolha == 'P': #JOGADOR ESCOLHEU PAR
        soma = num_jogador + computador
        par = soma % 2
        if par == 0: #GANHOU
            print('Você jogou {} e o computador jogou {}.'.format(num_jogador, computador))
            print(emojize('A soma dos valores é {}. É PAR :clap: '.format(soma), language='alias'))
            print(emojize('Parabés, você venceu! :trophy:', language='alias'))
            print('-' * 40)
        if par != 0: #PERDEU
            print('Você jogou {} e o computador jogou {}'.format(num_jogador, computador))
            print(emojize('A soma dos valores é {}. É ÍMPAR :sob:'.format(soma), language='alias'))
            cont = cont - 1
            if cont == 0:
                print('GAME OVER! Você não venceu nenhuma vez.')
            if cont == 1:
                print('GAME OVER! Você venceu 1 vez')
            if cont > 1:
                print('GAME OVER! Você venceu {} vezes'.format(cont))
            break
    if escolha == 'I': #JOGADOR ESCOLHEU ÍMPAR
        soma = num_jogador + computador
        par = soma % 2
        if par != 0: #GANHOU
            print('Você jogou {} e o computador jogou {}.'.format(num_jogador, computador))
            print(emojize('A soma dos valores é {}. É ÍMPAR :clap:'.format(soma), language='alias'))
            print(emojize('Parabéns, você venceu!:trophy:', language='alias'))
            print('-' * 40)
        if par == 0: #PERDEU
            print('Você jogou {} e o computador jogou {}.'.format(num_jogador, computador))
            print(emojize('A soma dos valores é {}. É PAR :sob:'.format(soma), language='alias'))
            cont = cont - 1
            if cont == 0:
                print('GAME OVER! Você não venceu nenhuma vez.')
            if cont == 1:
                print('GAME OVER! Você venceu 1 vez')
            if cont > 1:
                print('GAME OVER! Você venceu {} vezes'.format(cont))
            break













from random import randint
escolha = str(input('Vamos jogar par ou ímpar? Escolha [P/I]: ')).upper().strip()
n = int(input('Agora escolha um número entre 0 e 10: '))
nc = randint(0, 10)
s = n + nc
r = s % 2
cont = 0
fim = True
while fim:
    if escolha == 'I' and r != 0:
        print(f'Eu escolhi {nc} e você escolheu {n}, a soma das nossas escolha é {s} um número ímpar, logo você ganhou!')
        cont +=1
        escolha = str(input('Vamos jogar par ou ímpar? Escolha [P/I]: ')).upper().strip()
        n = int(input('Agora escolha um número entre 0 e 10: '))
        nc = randint(0, 11)
    elif escolha == 'P' and r == 0:
        print(f'Eu escolhi {nc} e você escolheu {n}, a soma das nossas escolha é {s} um número par, logo você ganhou!')
        escolha = str(input('Vamos jogar par ou ímpar? Escolha [P/I]: ')).upper().strip()
        n = int(input('Agora escolha um número entre 0 e 10: '))
        nc = randint(0, 10)
        cont +=1
    elif escolha == 'P' and r != 0:
        print(f'Eu escolhi {nc} e você escolheu {n}, a soma das nossas escolha é {s} um número ímpar, logo eu ganhei!')
        fim = False
    elif escolha == 'I' and r == 0:
        print(f'Eu escolhi {nc} e você escolheu {n}, a soma das nossas escolha é {s} um número par, logo eu ganhou!')
        fim = False
print(f'Agora você perdeu... mas antes disso ganhou {cont} vezes!')

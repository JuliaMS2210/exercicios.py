from time import sleep
from random import choice
pe = 'PEDRA'
pa = 'PAPEL'
te = 'TESOURA'
lista = [pe, pa, te]
print('Vamos jogar PEDRA, PAPEL OU TESOURA?')
sleep(2)
e = str(input('Escolha: ')).strip().lower()
j = choice(lista)
#caso o jogador escolha pedra
if e == 'pedra' and j == pa:
    print('HA, eu escolhi papel e ganhei!!!')
elif e == 'pedra' and j == te:
    print('Parabéns, eu escolhi tesoura e você ganhou!!!')
elif e == 'pedra' and j == pe:
    print('Que coisa, eu escolhi pedra e nós empatamos!!!')
#caso o jogador escolha papel
elif e == 'papel' and j == te:
    print('HA, eu escolhi tesoura e ganhei!!!')
elif e == 'papel' and j == pe:
    print('Parabéns, eu escolhi pedra e você ganhou!!!')
elif e == 'papel' and j == pa:
    print('Que coisa, eu escolhi papel e nós empatamos!!!')
#caso o jogador escolha tesoura
elif e == 'tesoura' and j == pe:
     print('HA, eu escolhi pedra e ganhei!!!')
elif e == 'tesoura' and j == pa:
    print('Parabéns, eu escolhi papel e você ganhou!!!')
elif e == 'tesoura' and j == te:
     print('Que coisa, eu escolhi tesoura e nós empatamos!!!')
bool

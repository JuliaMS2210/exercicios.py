num = int(input('digite um número inteiro: '))
c = int(input('Escolha uma base para conversão: \n 1- converter para BINÁRIO \n 2- converter para OCTAL \n 3- converter para HEXADECIMAL \n SUA RESPOSTA: '))
if c == 1:
    print('Conversão para BINÁRIO é igual a {}.'.format(bin(num)[2:]))
elif c == 2:
    print('Conersão para OCTAL é igual a {}.'.format(oct(num)[2:]))
elif c == 3:
    print('?Conversão para HEXADECIMAL é igual a {}.'.format(hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')
    
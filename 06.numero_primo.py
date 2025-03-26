n = int(input('Digite um número inteiro: '))
if n < 2:
    print('{} não é um número primo.'.format(n))
else:
    for c in range(2, n):
        if n % c == 0:
            print('{} não é um número primo.'.format(n))
            break
    else:
        print('{} é um número primo.'.format(n))

somai = 0
mediai = 0
maiorim = 0
nomevelho = ''
mulher20 = 0
print("-"*19)
print("Vou registrar alguns dados de 5 pessoas e avaliá-los:")
for p in range(1, 5):
    print('----- PESSOA {}-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somai += idade
    if p == 1 and sexo in 'Mm':
        maiorim = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorim:
        maiorim = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        mulher20 += 1
mediai = somai / 4
print('A média de idade do grupo é {} anos.'.format(mediai))
print('O homem mais velho tem {} anos e se {} chama. '.format(maiorim, nomevelho))
print('{} mulheres tem menos de 20 anos.'.format(mulher20))

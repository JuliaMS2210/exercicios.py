from datetime import date
print("Escolha um ano e direi se ele é bissexto.")
ano = int(input('Que ano você quer analizar? coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

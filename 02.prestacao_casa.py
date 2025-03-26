vc = int(float(input('Qual o valor da casa? ')))
s = int(float(input('Qual o valor do seu salário? ')))
anos = int(input('Em quantos anos você pretende pagar? '))
prestação = vc / (anos * 12)
minimo = s * 30 / 100
if prestação > minimo:
    print('Você não pode pagar por esta casa, ela passa de 30% do seu salário')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, o valor das prestações será de R${:.2f}.'.format(vc, anos, prestação))

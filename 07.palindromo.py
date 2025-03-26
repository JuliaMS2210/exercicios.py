f = str(input('Digite uma frase e descubra se ela é um palindromo: ')).strip().upper()
p = f.split()
junto = ''.join(p)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Essa palabra é um palindromo. ')
else:
    print('Essa palavra não é um palindromo. ')

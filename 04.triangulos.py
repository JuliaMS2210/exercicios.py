a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))
t = a < b + c and b < a + c and c < a + b
eq = a == b == c
i = a == b or b == c or c == a
es = a != b and b != c and c != a
if t and eq:
    print('Essas retas podem formar um triângulo equilátero.')
elif t and i:
    print('Essas retas podem formar um triângulo Isóceles.')
elif t and es:
    print('Essas retas podem formar um triângulo escaleno.')
else:
    print('Essas retas não formam um triângulo.')

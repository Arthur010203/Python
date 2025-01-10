from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = sqrt(co**2 + ca**2)
print('A hipotenusa tera o valor de {}'.format(h))

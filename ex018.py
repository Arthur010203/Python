from math import sin,cos,tan, radians
a = int(input('Escreva um ângulo qualquer: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O valor do seno de {} é {:.2f} seu cosseno é {:.2f} e sua tangente {:.2f}'.format(a, s, c, t))

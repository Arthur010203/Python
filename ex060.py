'''def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
         fatorial *= i
    return fatorial

# Entrada do usuário
num = int(input("Digite um número: "))

# Verifique se o número é negativo
if num < 0:
    print("Fatorial não existe para números negativos.")
else:
    print(f"O fatorial de {num} é {calcular_fatorial(num)}")'''

# Versão 1 do Guanabara

'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

# Versão 2 do Guanabara

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
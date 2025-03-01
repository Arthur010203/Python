n = int(input('Digite o primeiro número: '))
n1 = int(input('Digite o segundo número: '))
if n > n1:
    print('{} é maior do que {}'.format(n, n1))
elif n1 > n:
    print('{} é maior do que {}'.format(n1, n))
elif n1 == n:
    print('{} é igual a {}'.format(n1, n))

n = float(input('Digite a primeira nota: '))
n1 = float(input('Digite a segunda nota: '))
m = (n+n1)/2
if m < 5:
    print('Sua média final é {:.2f} REPROVADO'.format(m))
elif 5 <= m < 7:
    print('Sua média final é {:.2f} RECUPERAÇÃO'.format(m))
elif m >= 7:
    print('Sua média final é {:.2f} APROVADO'.format(m))

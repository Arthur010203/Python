s = float(input('Digite o valor do seu salário : '))
c = (10/100*s) + s
c1 = (15/100*s) + s
if s <= 1250:
    print('O seu salário atual é de {:.2f} R$'.format(c1))
else:
    print('O seu salário atual é de {:.2f} R$'.format(c))
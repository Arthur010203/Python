'''p1 = float(input('Digite o primeiro peso: '))
p2 = float(input('Digite o segundo peso: '))
p3 = float(input('Digite o terceiro peso:'))
p4 = float(input('Digite o quarto peso:  '))
p5 = float(input('Digite o quinto peso: '))

if p1 > p2 and p3 and p4 and p5:
    print('A pessoa mais pesada é a de {}kg '.format(p1))
elif p2 > p1 and p3 and p4 and p5:
    print('A pessoa mais pesada é a de {}kg'.format(p2))
elif p3 > p1 and p2 and p4 and p5:
    print('A pessoa mais pesada é a de {}kg'.format(p3))
elif p4 > p1 and p3 and p2 and p5:
    print('A pessoa mais pesada é a de {}kg'.format(p4))
elif p5 > p1 and p3 and p4 and p2:
    print('A pessoa mais pesada é a de {}kg'.format(p5))'''

# Versão do prof

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
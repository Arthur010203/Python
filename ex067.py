'''while True:
    numero = int(input('Digite um número para ver a tabuada (negativo para sair):'))

    if numero < 0:
        print("Programa encerrado. Até a próxima!")
        break

    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("-" * 30)'''

#  VERSÃO DO GUANABARA

while True:
    n = int(input('Quar ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

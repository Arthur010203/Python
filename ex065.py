''''# Programa para ler vários números e calcular média, maiore menor valor

soma = 0
quantidade = 0
maior = None
menor = None

while True:
    numero = int(input("Digite um número: "))
    soma += numero
    quantidade += 1

    # Define maior e menor na primeira entrada
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input("Resposta inválida. Quer continuar ? [S/N]: " ).strip().upper()
    if continuar == 'N' :
        break

media = soma / quantidade

print(f'\nVocê digitou {quantidade} números.')
print(f"A média foi {media:.2f}.")
print(f"O maior valor foi {maior} e o menor foi {menor}.")'''

# Versão do Guanabara

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            marior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior , menor))
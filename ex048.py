'''soma = 0
# Percorre os números de 1 até 500
for numero in range(1, 501):
    # Verifica se o número é ímpa e múltiplo de 3
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

# Exibe o resultado final
print("A soma de todos os números ímpares múltiplos de 3 de 1 até 500 é:", soma)'''

# Versão do prof

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c     #soma = soma + c
        cont += 1     #cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
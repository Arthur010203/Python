'''soma = 0

# Lê seis números inteiros
total_numeros = 6
for i in range(1, total_numeros + 1):
    numero = int(input(f'Digite o {i}° número inteiro: '))

    # Verifica se o númer é par e soma
    if numero % 2 == 0:
        soma += numero
# Exibe o resultado final
print('A soma dos números pares é:', soma)'''

# Versão do prof

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

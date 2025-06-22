''' # Lista principal com duas sublistas: [pares, ímpares]
numeros = [[], []]

# Loop para receber 7 números do usuário
for i in range(7):
     valor = int(input(f"Digite o {i+1}° valor: "))
     if valor % 2== 0:
         numeros[0].append(valor) # Pares na posição 0
     else:
         numeros[1].append(valor) # Ímpares na posição 1

# Ordenando as listas
numeros[0].sort()
numeros[1].sort()

# Exibindo os resultaodos
print(f"\nValores pares em ordem crescente: {numeros[0]}")
print(f"Vaores ímpares em ordem crescente: {numeros[1]}")
'''

# Versão do Guanabara
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]} ')
print(f'Os valores ímpares digitados foram: {núm[1]} ')
 # Lista principal com duas sublistas: [pares, ímpares]
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

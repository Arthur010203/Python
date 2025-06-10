# Lista para armazenar os números
valores = []

while True:
    num = int(input("Digite um número: "))
    valores.append(num)

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        break

# A) Quantos números foram digitados
quantidade = len(valores)

# B) Lista ordenada de forma decrescente
valores_decrescente = sorted(valores, reverse=True)

# C) Verificação se o número 5 está na lista
tem_cinco = 5 in valores

# Exibindo os resultados
print("\nRESULTADOS:")
print(f"A) Você digitou {quantidade} números.")
print(f"B) Os valores em ordem decrescente: {valores_decrescente}")
print(f"C) O valor 5 {'está' if tem_cinco else 'NÃO está'} na lista.")
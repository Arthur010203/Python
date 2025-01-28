#Programa para encontrar o maior e o menor número
print("Digite três números:")

# Entrada dos números
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))

# Verificando o maior número
maior = max(num1, num2, num3)

# Verificando o menor número
menor = min(num1, num2, num3)

# Exibindo os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
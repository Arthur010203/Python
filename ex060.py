def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n +1):
         fatorial *= i
    return fatorial

# Entrada do usuário
num = int(input("Digite um número: "))

# Verifique se o número é negativo
if num < 0:
    print("Fatorial não existe para números negativos.")
else:
    print(f"O fatorial de {num} é {calcular_fatorial(num)}")
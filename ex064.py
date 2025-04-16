# Programa para ler números até o usuário digitar 999

soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (999 para parar):"))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f"\n Você digitou {contador} números.")
print(f"A soma entre eles foi {soma}.")

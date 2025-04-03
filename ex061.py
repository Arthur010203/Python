# Entrada do usuário
primeiro_termo = int(input("Digite o primeiro termo da PA:"))
razao = int(input("Digite a razão da PA: "))

# Inicializando as variáveis
termo = primeiro_termo
contador = 1

# Estrutura de repetição while
while contador <= 10:
    print(f"Termo {contador}: {termo}")
    termo += razao # Próximo termo da PA
    contador += 1 # Incrementa ao contador
# Lista principal para armezenar os dados
pessoas = []
dados = []

while True:
    nome = input("Nome: ")
    peso = float(input("Peso (Kg): "))

    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:]) # Faz uma cópia da lista 'dados'
    dados.clear()

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Parte A: Quantas pessoas foram cadastradas
print(f"\nA) Total de pessoas cadastradas: {len(pessoas)}")

# Parte B e C: Encontrar os maiores e menores pesos
pesos = [p[1] for p in pessoas]
maior = max(pesos)
menor = min(pesos)

# Pessoas com maior peso
mais_pesadas = [p[0] for p in pessoas if p[1] == maior]
print(f"B) Maior peso foi {maior}kg. Peso de: {mais_pesadas}")

# Pessoas com menor peso
mais_leves = [p[0] for p in pessoas if p[1] == menor]
print(f"C) Menor peso foi {menor} kg. Pesos de: {mais_leves}")
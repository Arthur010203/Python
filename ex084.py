'''# Lista principal para armezenar os dados
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
print(f"C) Menor peso foi {menor} kg. Pesos de: {mais_leves}")'''

# Versão do Guanabara

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ' )
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg.Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

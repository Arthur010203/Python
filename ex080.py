# Lista para armazenar os valores em ordem
valores = []

for i in range(5):
    num = int(input(f'Digite o {i+1}° valor:'))

    # Se a lista estiver vazia ou o valor for maior que o último, adiciona no final
    if not valores or num > valores[-1]:
        valores.append(num)
        print("Adicionado ao final da lista.")
    else:
        # Procura a posição correta para inserir
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos += 1

# Mostrando a lista ordenada
print(f"\nOs valores digitados em ordem foram: {valores}")
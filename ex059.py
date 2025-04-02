def menu():
    print("\nEscolha uma opção:")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Maior")
    print("4 - Novos Números")
    print("5 - Sair")

while True:
    try:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")
        continue

    while True:
        menu()
        opcao =input("Opção escolhida: ")

        if opcao == '1':
            print(f"Resultado da soma: {valor1 + valor2}")
        elif opcao == '2':
            print(f"Resultado da multiplicação: {valor1 * valor2}")
        elif opcao == '3':
            maior = max(valor1, valor2)
            print(f"O maior valor é: {maior}")
        elif opcao == '4':
            break
        elif opcao == '5':
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")

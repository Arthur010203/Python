'''def menu():
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
'''

# Versão do Guanabara

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2 :
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)

print('Fim do programa! Volte sempre!')
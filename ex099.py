def maior(*numeros):
    if len(numeros) == 0:
        print("Nenhum número foi informado")
        return

    maior_num = numeros[0]
    print("Analisando os valores passados...")
    for num in numeros:
        print(num, end=' ')
        if num > maior_num:
            maior_num = num
        print(f"\nO maior valor informado foi {maior_num}.\n")

# Testes da função
maior(1, 5, 3, 9, 2)
maior(10, 20)
maior()
maior(7)
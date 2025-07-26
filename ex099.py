'''def maior(*numeros):
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
maior(7)'''

# Versão do Guanabara
from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}. ')

# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
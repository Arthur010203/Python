''''# Lê quatro valores do teclado e armazena na tupla
valores = tuple(int(input(f"Digite o {i+1} número:")) for i in range(4))

# Mostra a tupla completa
print(f"\nVocê digitou os valores: {valores}")

# A) Quantas vezes apareceu o valor 9
quant_nove = valores.count(9)
print(f"A) O número 9 apareceu {quant_nove} vez(es).")

# B) Em que posição foi digitado o primeiro valor 3
if 3 in valores:
    posicao_tres= valores.index(3) + 1 # +1 para mostrar posição "humana"
    print(f"B) O número 3 apareceu na {posicao_tres}ª posição.")
else:
    print("B) O número 3 não foi digitado.")

# C) Quais foram os números pares
pares = tuple(valor for valor in valores if valor % 2 == 0)
print(f"C) Os números pares digitados foram: {pares if pares else 'Nenhum'}")'''

# Versão do Guanabara

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end='')
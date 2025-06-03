# Lê quatro valores do teclado e armazena na tupla
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
print(f"C) Os números pares digitados foram: {pares if pares else 'Nenhum'}")
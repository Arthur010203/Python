'''n = int(input("Quantos termos da Sequência de Fibonacci você deseja ver ? "))

#Verifica se o número é válido
if n <= 0:
    print("Por favor, insira um número maior que zero.")
else:
    # Inicializandoa os primeiros termos
    termo1, termo2 = 0, 1
    contador = 1

    print("Sequência de Fibonacci:")
    while contador <= n :
        print(termo1, end=" ") # Exibe o termo atual
        proximo_termo = termo1 + termo2 # Calcula o próximo termo
        termo1, termo2 = termo2, proximo_termo # Atualiza os valores
        contador += 1 # Incrementa o contador'''

# Versão do Guanabara

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*30)

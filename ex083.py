# Leitura da expressão
expressao = input("Digite uma expressão com parênteses: ")

# Pilha para verificar o balanceamento dos parênteses
pilha = []

# Analisando cada caractere da expressão
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break # Parêntese fechado sem correspondente aberto

# Verificação final
if len(pilha) == 0:
    print("A expressão está com os parênteses corretos!")
else:
    print("A expressão está com os parêntese incorretos!")
# Verifica se um ano é bissexto

ano = int(input("Digite um ano: "))

if (ano %4 == 0 and ano %100 != 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f"O ano {ano} não é bissexto.")
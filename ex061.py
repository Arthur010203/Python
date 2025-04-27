''''# Entrada do usuário
primeiro_termo = int(input("Digite o primeiro termo da PA:"))
razao = int(input("Digite a razão da PA: "))

# Inicializando as variáveis
termo = primeiro_termo
contador = 1

# Estrutura de repetição while
while contador <= 10:
    print(f"Termo {contador}: {termo}")
    termo += razao # Próximo termo da PA
    contador += 1 # Incrementa ao contador'''

# Versão do Guanabara

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}    ->    '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
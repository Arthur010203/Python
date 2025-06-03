'''from datetime import datetime

# Obtém o ano atual
ano_atual = datetime.now().year

# Inicializa os contadores
maiores = 0
menores = 0

# Lê o ano de nascimento de sete pessoas
for i in range(1, 8):
    ano_nascimento= int(input(f'Digite o ano de nascimento da {i}ª pessoa:'))
    idade = ano_atual - ano_nascimento

    # Verifica se a pessoa é maior de idade
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
# Exibe o resultado final
print(f'Total de pessoas maiores de idade: {maiores}')
print(f'Total de pessoas menores de idade: {menores}')'''

# Versão do prof

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pesoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

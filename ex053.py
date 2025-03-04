''' # Verificar se uma frase é um palíndromo

# Leitura da frase
frase = input ('Digite uma frase: ').replace('', '').lower()

# Verificação de palíndromo
if frase == frase[::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')'''

# Versão do prof

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndrome!')
else:
    print('A frase digitada não é um palíndromo!')'''

# Versão resumida do prof

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
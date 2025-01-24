'''frase = str(input('Escreva uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('a')))
print('A letra "A" aparece pela pela primeira vez na posição {} da frase'.format(frase.find('a')+1))
print('A ultima posição em que a letra "A" aparece é a {}'.format(frase.rfind('a')+1))'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')+1))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

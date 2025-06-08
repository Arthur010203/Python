'''palavras =  (
    'banana', 'computador', 'livro', 'cadeira',
    'garrafa', 'telefone', 'janela', 'mochila'
)

vogais = 'aeiou'

print('-' * 40)
print(f'{"VOGAIS EM CADA PALAVRA":^40}')
print('-' * 40)

for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}" temos:', end=' ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end =' ')
print('\n' + '-' * 40)'''

# Versão do Guanabara

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= '')
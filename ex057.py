'''def obter_sexo():
    opcoes_validas = {'M', 'F', 'B', 'NB','@', 'X' }
    while True:k
        sexo = input("Digite o sexo (M, F, B, NB): ").strip().upper()
        if sexo in opcoes_validas:
            return sexo
        else:
            print("Entrada inválida! Por favor, digite apenas 'M', 'F', 'B', '@', 'X' ou 'NB'.")

# Chamando a função
genero = obter_sexo()
print(f"Você selecionou: {genero}")'''

# Versão do professor Guanabara

sexo = str(input('Informe seu sexo: [M/F/@/X/NB/B]')).strip().upper()[0]
while sexo not in 'MmFf@XxNBnbBb':
    sexo = str(input('Dadaos inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
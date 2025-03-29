def obter_sexo():
    opcoes_validas = {'M', 'F', 'B', 'NB'}
    while True:
        sexo = input("Digite o sexo (M, F, B, NB): ").strip().upper()
        if sexo in opcoes_validas:
            return sexo
        else:
            print("Entrada inválida! Por favor, digite apenas 'M', 'F', 'B' ou 'NB'.")

# Chamando a função
genero = obter_sexo()
print(f"Você selecionou: {genero}")
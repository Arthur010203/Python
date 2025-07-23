def escreva(texto):
    '''
    Exibe uma mensagem com uma moldura de traços adaptável ao temanho do texto

    Parâmetro:
    texto (str): A mensagem que será exibida.
    '''

    tamanho = len(texto)
    print('-' * (tamanho + 4))
    print(f' {texto}')
    print('-' * (tamanho + 4))

# Programa principal
escreva('Olá, Mundo!')
escreva('Programação em Python')
escreva('Arthur')
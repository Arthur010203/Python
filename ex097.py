'''def escreva(texto):

    Exibe uma mensagem com uma moldura de traços adaptável ao temanho do texto

    Parâmetro:
    texto (str): A mensagem que será exibida.


    tamanho = len(texto)
    print('-' * (tamanho + 4))
    print(f' {texto}')
    print('-' * (tamanho + 4))

# Programa principal
escreva('Olá, Mundo!')
escreva('Programação em Python')
escreva('Arthur')'''

# Versão do Guanabara

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'    {msg}')
    print('~'*tam)

# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
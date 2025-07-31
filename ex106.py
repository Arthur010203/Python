def titulo(msg, cor=0):
    cores = [
        '\033[m', # 0 - Sem cor
        '\033[0;30;41m',    # 1 - Vermelho
        '\033[0;30;42m',    # 2 - Verde
        '\033[0;30;43m',    # 3 - Amarelo
        '\033[0;30;44m',    # 4 - Azul
        '\033[0;30;45m',    # 5 - Roxo
        '\033[7,30'         # 6 - Branco invertido
    ]
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~'* tam)
    print(f'{msg}')
    print('~' * tam)
    print('\033[m', end='') # Reset de cor

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print('\033[7;30m', end='') # Fundo branco, testo preto
    help(comando)
    print('\033[m', end='')   # Rest de cor


# Prorama Principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)
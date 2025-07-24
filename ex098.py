from time import sleep

def contador(inicio, fim, passo):
    '''

    Realaiza uma contagem de acordo com os parâmetros fornecidos.

    Parâmentros:
    inicio(int): Valor incial da contagem.
    fim(int): Valor final da contagem.
    passo (int): Paddo da contagem(incremento ou decremento).
    '''
    print('-' * 40)
    print(f'Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')

    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end='', flush=True)
            sleep(0.3)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end='', flush=True)
            sleep(0.3)
            cont -= passo
    print('\n' + '-' * 40)

# Contagen s solicitadas:
contador(1, 10, 1)
contador(10, 0, 2)

# Contagem personalizada
print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)


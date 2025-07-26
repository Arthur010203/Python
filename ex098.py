'''from time import sleep

def contador(inicio, fim, passo):


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
contador(ini, fim, pas)'''

# Versão do Guanabara
from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa principal
contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)


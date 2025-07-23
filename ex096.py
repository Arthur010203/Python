def area(largura, comprimento):
    '''

    Função que calcula e exibe a aárea de um terreno retangular.

    Parâmetros:
    largura (float): A largura do terreno em metros.
    comprimento (float): O comprimento do terreno em metros.
    '''

    resultado = largura * comprimento
    print(f'A área de um terreno {largura}m  x {comprimento}m é de {resultado}m².')

# Programa principal
print('Controle de Terrenos')
print('-' * 30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
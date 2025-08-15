""" def aumentar(preco=0, taxa=0):

    Docstring
    Aumenta o preço em uma determinada porcentagem.
    :param preco: Valor original
    :param taxa: Porcentagem de aumento
    :return: Novo preço com aumento

    return preco + (preco * taxa / 100)

def diminuir(preco=0, taxa=0):

    Docstrings
    Diminui o preço em uma determinada porcentagem.
    :param preco:  Valor original
    :param taxa: Porcentagem de redução
    :return: Novo preço com desconto

    return preco - (preco * taxa / 100)

def dobro(preco=0):

    Retorna o dobro do preço.

    return preco * 2

def metade (preco=0):

    Retorna a metade do preço.

    return preco / 2 """

# Versão do Guanabara

def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
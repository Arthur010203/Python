"""def aumentar(preco=0, taxa=0):

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

    return preco / 2"""

# Versão do Guanabara

def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res

def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço):
    res = preço * 2
    return res

def metade(preço):
    res = preço / 2
    return res
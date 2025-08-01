'''def notas(*n, situacao=False):
   Docstring
    Calcula estatísticas sobre as notas de uma turma.

    Parâmetros:
    *n: uma ou mais notas dos alunos (valores numéricos)
    situacao : valor opcional (padrão False). Se True, inclui a situação da turma no retorno.

    Retorna:
    dict : um dicionário contendo:
        - total: quantidade de notas
        - maior: maior nota
        - menor: menor nota
        - media: média das notas
        - situacao: (opcional) situação geral da turma

    resultado = dict()
    resultado['total'] = len(n)
    resultado['maior'] = max(n)
    resultado['menor'] = min(n)
    resultado['media'] = sum(n) / len(n)

    if situacao:
        if resultado['maior'] >= 7:
            resultado['situacao'] = 'Boa'
        elif resultado['media'] >= 5:
            resultado['sitacao'] = 'Razoável'
        else:
            resultado['situacao'] = 'Ruim'

    return resultado

# Exemplo de uso:
resp = notas(2, 3, 4, 4.2, situacao=True)
help(notas()) '''

# Versão do Guanabara

def notas(*n , sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa Principal
resp = notas(9, 6, 9.5, sit=True)
print(resp)
help(notas)
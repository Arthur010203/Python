def notas(*n, situacao=False):
    """
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
    """
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
help(notas())
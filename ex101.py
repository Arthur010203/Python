from datetime import date

'''def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return "VOTO NEGADO"
    elif 16 <= idade < 18 or idade > 70:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"

# Programa principal
nascimento = int(input("Digite o ano de nascimento: "))
situacao = voto(nascimento)
print(f"Para quem nasceu em {nascimento}, a situação do voto é: {situacao}")'''

# Versão do Guanabara

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
from datetime import date

def voto(ano_nascimento):
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
print(f"Para quem nasceu em {nascimento}, a situação do voto é: {situacao}")
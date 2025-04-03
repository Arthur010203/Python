# Entrada do usuário
primeiro_termo = int(input("Digite o primeiro termo da PA:"))
razao = int(input("Digite a razão da PA: "))

# Inicializando variáveis
termo = primeiro_termo
contador = 1
total_termos = 10 # Inicialmente mostra 10 termos
mais_termos = 10 # Quantidade de termos adicionais a serem exibidos

# Estrutura de repetição while
while mais_termos != 0:
    while contador <= total_termos:
        print(f"Termo{contador}: {termo}")
        termo += razao # Próximo termo da PA
        contador += 1 # Incrementa o contador

    # Pergunta ao usuário se deseja mostrar mais termos
    mais_termos = int(input("Quantos termos você quer mostrar a mais? (Digite 0 pararr sair): "))
    total_termos += mais_termos # Atualiza o total de termos a serem exibidos

print("Programa encerrado.")
# Versão do Orion
'''import csv

def main():
    """
    Programa para gerenciar notas e gerar um boletim.

    """

    # Criando a lista de alunos
    alunos = []
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar):")
        if nome == "sair":
            break
        nota1 = float(input("Digite a primeira nota:"))
        nota2 = float(input("Digite a segunda nota:"))
        alunos.append({
            "nome": nome,
            "notas": [nota1, nota2]
        })

    # Salva os dados em um arquivo CSV (você pode customizar o nome do arquivo)
    with open('boletim.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['nome', 'notas'])
        writer.writeheader()
        for aluno in alunos:
            writer.writerow(aluno)

    # Mostra um boletim com a média das notas dos alunos
    print("Boletim:")
    print("-" * 30)
    print(f"Alunos cadastrados: {len(alunos)}")

if __name__ == "__main__":
    main()'''

# Versão do Guanabara
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZADO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
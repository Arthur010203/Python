from arquivo import criarArquivo
from cadastro import novoCadastro, listarCadastros

ARQUIVO = "pessoas.txt"

criarArquivo(ARQUIVO)

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Cadastrar nova pessoa")
    print("2 - Listar pessoas cadastradas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novoCadastro(ARQUIVO)
    elif opcao == "2":
        listarCadastros(ARQUIVO)
    elif opcao == "3":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
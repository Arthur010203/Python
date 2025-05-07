print("==== CAIXA ELETRÔNICO ====")

# Solicita o valor a ser sacado
valor = int(input("Informe o valor a ser sacado: R$ "))

# Inicializa as cédulas disponíveis
cedulas = [50, 20, 10, 1]

# Calcula e exibe quantas cédullas de cada valor serão entregues
for cedula in cedulas:
    quantidade = valor // cedula
    valor = valor % cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R$ {cedula} ")

print("=== FIM DA OPERAÇÃO ===")

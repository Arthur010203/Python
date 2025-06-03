numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    try:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <=20:
            print(f"Você digitou o número {numeros[num]}.")
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada iválida. Por favor, digite um número inteiro.")

# Versão do Guanabara

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
         break
    print('Tente novamente. ', end='')
print(f'Você digitouo número {cont[núm]}')
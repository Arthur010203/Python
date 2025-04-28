''''# Programa para ler números até o usuário digitar 999

soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (999 para parar):"))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f"\n Você digitou {contador} números.")
print(f"A soma entre eles foi {soma}.")
'''

#Versão do Guanabara

núm = cont = soma = 0
núm = int(input('Dgite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} número e a soma entre eles foi {}.'.format(cont, soma))
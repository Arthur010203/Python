'''v = cont = soma = 0
v = int(input('Digite um valor (999 para parar):'))
while v != 999:
    soma += v
    cont += 1
    v = int(input('Digite um valor (999 para parar):'))
print(f'Você digitou {cont} valores a soma deles é de {soma}')'''

# VERSÃO DO GUANABARA

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
'''mais_18 = 0
homens = 0
mulheres_menos_20 = 0

print("===== CADASTRO DE PESSOAS =====")

while True:
    idade = int(input("idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    while sexo not in ['M', 'F']:
        sexo = input("Entrada inválida. Sexo [M/F]: ").strip().upper()

    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input("Entrada inválida. Deseja continuar? [S/N]: ").strip().upper()

    if continuar == 'N':
        break

print("\n===== RESEULTADOS =====")
print(f"A) Total de pessoas com mais de 18 anos: {mais_18}")
print(f"B) Total de homens cadsastrados: {homens}")
print(f"C) Total de mulheres com menos de 20 anos: {mulheres_menos_20}")'''

# Versão do Guanabara
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper() [0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
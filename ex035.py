a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if (a + b > c) & (a + c > b) & (b + c > a):
    print("É possível se formar um triangulo com esses valores que você dispos")
else:
    print("Não é possível se formar um triângulo com esses valores")
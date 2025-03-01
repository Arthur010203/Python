peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
IMC = peso/altura**2
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC <= 25 :
    print('Peso ideal')
elif IMC > 25 and IMC < 30:
    print('Sobrepeso')
elif IMC > 30 and IMC < 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade mórbida')
# Versão Original
'''v = int(input('A quantos km/h o carro está ? '))
l = 80
m = 7
if v > 80:
    print('Você foi multado, a multa vai custar {}R$'.format((v-l)*m))'''

# Versão do Guanabara

velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia ! Dirija com segurança!')





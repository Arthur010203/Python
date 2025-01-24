''''nome = str(input('Digite seu nome completo: ')).split()
print('Muito prazer em te conhecer ! \n Seu primeiro nome é {} \n Seu último nome é {}'
      .format(nome[0], nome[-1]))'''

n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))


'''num = int(input('Digite um número para ver sua tabuada: '))
print('(>‿◠)✌' * 12)

# Utilizando um laço for para a tabuada
for i in range(1, 11):
    print('{} x {:.2} = {}'.format(num, i, num * i))

print('✍(◔◡◔)' * 12)'''

# Versão do prof

num = int(input('Digite um número para ver sua tabuada: '))
for c in range (1,11):
    print('{} X {:2} = {}'.format(num, c, num*c))

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end= ' -> ')
print('ACABOU')
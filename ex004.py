a = input('Enter something: ')
print('The primitive type of this value is ', type(a))
print('{} has only spaces?'.format(a), a.isspace())
print('{} is a number?'.format(a), a.isnumeric())
print('{} is alphabetic?'.format(a), a.isalpha())
print('{} is uppercase?'.format(a), a.isupper())
print('{} is lowercase?'.format(a), a.islower())
print('{} is capitalized?'.format(a), a.istitle())

nome = input('Qual seu primeiro nome? ')

sobrenome = input('Qual seu sobrenome? ')

logradouro = input('Qual seu endereço sem o número? ')

numero = input('Qual o número da residência? ')

bairro = input('Qual o bairro? ')

cidade = input('Qual a cidade? ')

estado = input('Qual o estado? ')

print(f'{'#' * 10} Suas informações são {'#' * 10}')

print(f'Prezado(a), {nome.capitalize() + '' + sobrenome.title()}')
print(f'Sua residência está localizada no endereço {logradouro.title() + ', ' + numero}')
print(f'Situada no bairro {bairro.title()}, {cidade.title()} - {estado.upper()}')

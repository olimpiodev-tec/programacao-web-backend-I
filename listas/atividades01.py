cores = ['azul', 'amarelo', 'vermelho', 'verde']
numero = int(input('Digite um número de 0 até 3'))

print(cores)
print(cores[numero])

numeros = [34, 89, 3, 45, 12, 78, 56, 345]
fator = int(input('Digite um fator de multiplicação'))
numeros_calculados = []

for numero in numeros:
    resultado = numero * fator
    numeros_calculados.append(resultado)

for resultado in numeros_calculados:
    print(resultado)


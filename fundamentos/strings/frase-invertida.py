frase = input('Prezado usuário digite uma frase: ')

frase_invertida = ""

qtde_frase = len(frase) - 1

vogais = ['a', 'e', 'i', 'o', 'u']

qtde_vogais = 0

for index in range(qtde_frase, -1, -1):
    frase_invertida += frase[index]

    if frase[index] in vogais:
        qtde_vogais += 1

print(f'A frase original é {frase}')
print(f'A frase invertida é {frase_invertida}')
print(f'A quantidade de vogais é {qtde_vogais}')

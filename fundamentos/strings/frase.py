frase = input('Prezado usuário digite uma frase: ')

qtde_caracteres = len(frase)

frase_sem_espacos = frase.strip()

qtde_caracteres_sem_espacos = len(frase_sem_espacos)

palavras = frase.split(' ')

qtde_palavras = len(palavras)

print(f'A frase {frase} tem {qtde_caracteres} caracteres')
print(f'A frase {frase_sem_espacos} tem {qtde_caracteres_sem_espacos} caracteres')
print(f'A frase {frase} tem {qtde_palavras} palavras')
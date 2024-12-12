cardapio_almoco_md = [
    'Big Mac', 'Quarteirão', 'MC Lanche Feliz'
]

cardapio_almoco_preco_md = [
    16.99, 19.99, 9.99
]

cardapio_refri_md = [
    'Coca cola', 'Sprite', 'Suco Uva'
]

cardapio_refri_preco_md = [
    12.99, 11.99, 14.99
]

cardapio_sobremesa_md = [
    'Casquinha', 'MC Colosso', 'Tortinha'
]

cardapio_sobremesa_preco_md = [
    3.99, 9.99, 7.99
]

pedidos = []
total = 0

print('Caro cliente, veja o nosso cardápio de hoje\n')

for item in range(0, 3):
    op_lanche = f'Opção {item}: Lanche {cardapio_almoco_md[item]}'
    v_lanche = f'R$ {cardapio_almoco_preco_md[item]}'
    print(f'{op_lanche} {v_lanche}')

print('\nAgora selecione 3 opções do cardápio')

for item in range(0, 3):
    opcao = int(input('Qual a opção escolhida?'))
    if opcao == 0:
        pedidos.append('Big Mac')
        total += 16.99
    if opcao == 1:
        pedidos.append('Quarteirão')
        total += 19.99
    if opcao == 2:
        pedidos.append('MC Lanche Feliz')
        total += 9.99

print('Caro cliente, agora escolha uma opção de bebida\n')

for item in range(0, 3):
    op_refri = f'Opção {item}: Refri {cardapio_refri_md[item]}'
    v_refri = f'R$ {cardapio_refri_preco_md[item]}'
    print(f'{op_refri} {v_refri}')

print('\nAgora selecione 3 opções de refrigerante')

for item in range(0, 3):
    opcao = int(input('Qual a opção escolhida?'))
    if opcao == 0:
        pedidos.append('Coca cola')
        total += 12.99
    if opcao == 1:
        pedidos.append('Sprite')
        total += 11.99
    if opcao == 2:
        pedidos.append('Suco de Uva')
        total += 14.99

print('Caro cliente, agora escolha uma opção de sobremesa\n')

for item in range(0, 3):
    op_sobre = f'Opção {item}: Sobremesa {cardapio_sobremesa_md[item]}'
    v_sobre = f'R$ {cardapio_sobremesa_preco_md[item]}'
    print(f'{op_sobre} {v_sobre}')

print('\nAgora selecione 3 opções de sobremesa 😊')

for item in range(0, 3):
    opcao = int(input('Qual a opção escolhida?'))
    if opcao == 0:
        pedidos.append('Casquinha')
        total += 3.99
    if opcao == 1:
        pedidos.append('MC Colosso')
        total += 9.99
    if opcao == 2:
        pedidos.append('Tortinha')
        total += 7.99

print('Prezado cliente, segue as informações para pagamento')
print(f'Seu pedido {pedidos}')
print(f'Total de R$ {total:.2f}')

dividir = int(input('Deseja dividir a conta? [0] Não [1] Sim'))

if dividir == 1:
    qtde_pessoas = int(input('Quantas pessoas?'))
    total_pessoa = total / qtde_pessoas
    print(f'O total por pessoa é R$ {total_pessoa:.2f}')
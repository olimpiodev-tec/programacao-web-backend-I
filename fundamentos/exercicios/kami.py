cadernos = [
    'Caderno 10 matérias', 'Caderno desenho', 'Caderno 1 matéria'
]

cadernos_valor = [
    15.50, 4.40, 6.49
]

canetas = [
    'Caneta Bic Azul', 'Caneta Gel', 'Caneta Esferográfica Bazze Wave 1.0 Mini Tris'
]

canetas_valor = [
    1.90, 8.90, 2.10
]

lapis = [
    'Lápis De Escrita Colorido Ilimitado',
    'Lápis de escrever apontado',
    'Lápis para Escrever'
]

lapis_valor = [
    3.00, 1.60, 0.68
]

print('Seja bem vindo querido cliente, entre na nossa loja e aproveite os descontos 😊\n')

print('Veja nossa lista de cadernos com super desconto\n')
for item in range(0, 3):
    print(f'Opção {item}: {cadernos[item]} R$ {cadernos_valor[item]}')

opcao_caderno = int(input('Agora escolha 1 opção de caderno\n'))

lista = []
total = 0

if opcao_caderno == 0:
    lista.append('Caderno 10 matérias')
    total += 15.50
elif opcao_caderno == 1:
    lista.append('Caderno desenho')
    total += 4.40
elif opcao_caderno == 2:
    lista.append('Caderno 1 matéria')
    total += 6.49

print('Agora veja as opções de canetas com mega desconto')

for item in range(0, 3):
    print(f'Opção {item}: {canetas[item]} R$ {canetas_valor[item]}')

opcao_caneta = int(input('Agora escolha 1 opção de caderno\n'))

if opcao_caneta == 0:
    lista.append('Caneta Bic Azul')
    total += 1.90
elif opcao_caneta == 1:
    lista.append('Caneta Gel')
    total += 9.90
elif opcao_caneta == 2:
    lista.append('Caneta Esferográfica Bazze Wave 1.0 Mini Tris')
    total += 2.10

print('Agora veja as opções de lápis com hiper mega desconto')

for item in range(0, 3):
    print(f'Opção {item}: {lapis[item]} R$ {lapis_valor[item]}')

opcao_lapis = int(input('Agora escolha 1 opção de lapis\n'))

if opcao_lapis == 0:
    lista.append('Lápis De Escrita Colorido Ilimitado')
    total += 3.00
elif opcao_lapis == 1:
    lista.append('Lápis de escrever apontado')
    total += 1.60
elif opcao_lapis == 2:
    lista.append('Lápis para Escrever')
    total += 0.68

parcelar = int(input('Deseja parcelar a compra? [0] Não [1] Sim'))

print('Caro cliente obrigado por comprar na nossa papelaria estamos muito felizes em revê-lo')
print(f'Itens comprados: {lista}')

if parcelar == 0:
    print(f'Total da compra R$ {total:.2f}')
elif parcelar == 1:
    parcelas = int(input('Quantas parcelas?'))
    v_parcela = total / parcelas
    print(f'Total de cada parcela é R$ {v_parcela:.2f}')

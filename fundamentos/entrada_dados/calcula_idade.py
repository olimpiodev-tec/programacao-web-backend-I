nome = input("Digite seu nome: ")
data_nascimento = int(input("Qual o ano que você nasceu? "))
data_fixa = 2024

anos = data_fixa - data_nascimento
meses = anos * 12
dias = anos * 365

print(f"Obrigado {nome}, você tem {anos}, {meses}, {dias}")

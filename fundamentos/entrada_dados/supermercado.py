produto = input("Digite o nome do produto: ")
valor = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o valor do desconto: "))

valor_desconto = valor - desconto

print(f"O valor do produto com desconto é {valor_desconto}")
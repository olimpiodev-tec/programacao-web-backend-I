qtde_reais = float(input("Digite a qtde de reais que você quer converter: "))
valor_dolar = float(input("Digite o valor do dólar: "))
valor_reais_convertido = qtde_reais / valor_dolar

print(f"R$ {qtde_reais} equivalem à {valor_reais_convertido:.2f} dolár")
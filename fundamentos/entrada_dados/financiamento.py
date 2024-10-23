preco_imovel = float(input("Digite o preço do seu imóvel: "))
parcelas = int(input("Digite o número de parcelas que deseja pagar: "))
valor_parcela = preco_imovel / parcelas

print(f"O total de cada parcela será de R$ {valor_parcela:.2f}")

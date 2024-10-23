"""
Exemplo de cálculo de financiamento imobiliário
considerando o valor do imóvel, período em anos.
Estamos desconsiderando os juros, parcelas iguais.
"""
valor_imovel = 560000.00
periodo = 30

total_meses = periodo * 12
valor_parcela = valor_imovel / total_meses

print(f"O imóvel com valor de R$ {valor_imovel:.2f}"
      f" parcelado em {total_meses} será pago"
      f" com R$ {valor_parcela:.2f} por mês")
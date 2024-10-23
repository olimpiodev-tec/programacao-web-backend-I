"""
Exemplo de algoritmo que calcula o custo da viagem
para os combustíveis gasolina e etanol.
Vamos usar o valor do litro dos combustíveis como
constantes para praticar, vamos lá :)
"""
carro = "Onix Sedan 1.6 Automático Turbo"
VALOR_LITRO_GASOLINA = 5.69
VALOR_LITRO_ETANOL = 3.49
MEDIA_KM_LTS_GASOLINA = 12
MEDIA_KM_LTS_ETANOL = 9

cidade_saida = "Piracicaba"
cidade_destino = "São José dos Campos"
kilometros = 221

qtde_litros_gasolina = kilometros / MEDIA_KM_LTS_GASOLINA
qtde_litros_etanol = kilometros / MEDIA_KM_LTS_ETANOL

valor_gasto_gasolina = qtde_litros_gasolina * VALOR_LITRO_GASOLINA
valor_gasto_etanol = qtde_litros_etanol * VALOR_LITRO_ETANOL

print("---Relatório de viagem---")
print(f"Saindo de {cidade_saida}, indo para {cidade_destino}")
print(f"Será gasto R$ {valor_gasto_gasolina:.2f} com gasolina")
print(f"Será gasto R$ {valor_gasto_etanol:.2f} com etanol")
print("Tenha uma excelente viagem :)")


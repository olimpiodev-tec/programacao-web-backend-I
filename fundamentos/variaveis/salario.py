"""
Exemplo de algoritmo que calcula o aumento
de salário do colaborador baseando se
no percentual do aumento.
"""
colaborador_nome = "Moisés Olimpio"
empresa = "Senai"
salario = 3456.90
percentual = 7
valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento

print(f"O colaborador {colaborador_nome}, trabalha"
      f" na empresa {empresa} e foi promovido com novo"
      f" salário de R$ {novo_salario:.2f}")

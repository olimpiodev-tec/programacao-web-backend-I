gasolina = float(input("Qual valor gasto com gasolina? "))
km = gasolina / 3.50
hospedagem = float(input("Qual valor gasto em hospedagem? "))
comida = float(input("Qual valor gasto com comida? "))
compras = float(input("Qual gasto com compras ? "))

valor_final = comida + hospedagem + compras + gasolina

print(f"O custo da sua viagem foi R$ {valor_final}\n"
      f"E foram rodados {km:.2f}")

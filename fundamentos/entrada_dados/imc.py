peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura**2)

print(f"O usuário possui IMC {imc:.2f}%")
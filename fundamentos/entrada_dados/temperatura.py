print("Olá sou um conversor de temperatura")

escolha = input("Digite se você escolher graus Celsius ou Fahrenheit: ")

if escolha == "celsius":
    graus = float(input("Digite a temperatura: "))
    transformar = (graus * 9 / 5) + 32
    print(f"A temperatura em fahrenheit será {transformar:.2f}")
elif escolha == "fah":
    fah = float(input("Digite a temperatura: "))
    transformar = (fah - 32) * 5 / 9
    print(f"A temperatura em celsius será {transformar:.2f}")
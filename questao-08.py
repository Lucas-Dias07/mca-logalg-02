moedas_10 = int(input("Quantidade de moedas de R$ 0,10: "))
moedas_25 = int(input("Quantidade de moedas de R$ 0,25: "))
moedas_50 = int(input("Quantidade de moedas de R$ 0,50: "))

total = (moedas_10 * 0.10) + (moedas_25 * 0.25) + (moedas_50 * 0.50)

print(f"Total poupado: R$ {total:.2f}")

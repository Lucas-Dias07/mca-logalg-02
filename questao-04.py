quantidade_paineis = int(input("Digite a quantidade de painéis: "))
valor_kwh = float(input("Digite o valor do kWh: R$ "))

geracao_diaria = quantidade_paineis * 1.2
geracao_mensal = geracao_diaria * 30

economia = geracao_mensal * valor_kwh

print(f"Geração em 30 dias: {geracao_mensal:.2f} kWh")
print(f"Economia no mês: R$ {economia:.2f}")

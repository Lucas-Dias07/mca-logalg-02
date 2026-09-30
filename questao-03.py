peso_saco = float(input("Digite o peso do saco de ração em kg: "))
consumo_diario = float(input("Digite o consumo diário em gramas: "))

peso_em_gramas = peso_saco * 1000

consumo_5_dias = consumo_diario * 5

sobra = peso_em_gramas - consumo_5_dias

print(f"Quantidade de ração que sobrará: {sobra:.2f} g")

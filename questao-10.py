total_moedas = int(input("Digite a quantidade total de moedas: "))
exploradores = int(input("Digite o número de exploradores: "))

moedas_por_explorador = total_moedas // exploradores
moedas_sobrando = total_moedas % exploradores

print("Cada explorador receberá:", moedas_por_explorador, "moedas")
print("Moedas para o líder:", moedas_sobrando)

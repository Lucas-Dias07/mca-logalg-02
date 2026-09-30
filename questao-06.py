quantidade = int(input("Digite a quantidade de capinhas produzidas: "))
preco_venda = float(input("Digite o preço de venda de cada capinha: R$ "))

materia_prima = 3.50
mao_de_obra = 1.50
embalagem = 0.80

custo_unitario = materia_prima + mao_de_obra + embalagem

custo_total = quantidade * custo_unitario

valor_vendas = quantidade * preco_venda

lucro = valor_vendas - custo_total

print(f"Custo total de produção: R$ {custo_total:.2f}")
print(f"Lucro líquido: R$ {lucro:.2f}")

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura

litros_tinta = area / 3

print(f"Área da parede: {area:.2f} m²")
print(f"Quantidade de tinta necessária: {litros_tinta:.2f} litros")

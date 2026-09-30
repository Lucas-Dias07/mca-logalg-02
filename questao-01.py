pocoes_cura = int(input("Digite a quantidade de poções de cura: "))
pocoes_energia = int(input("Digite a quantidade de poções de energia: "))

mana_cura = pocoes_cura * 15
mana_energia = pocoes_energia * 25

total_mana = mana_cura + mana_energia

print("Total de mana gerado:", total_mana)

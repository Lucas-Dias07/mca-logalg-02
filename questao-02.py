total_arrecadado = float(input("Digite o valor total arrecadado: R$ "))

valor_guardado = total_arrecadado * 0.10
valor_restante = total_arrecadado - valor_guardado

valor_cada_amigo = valor_restante / 3

print(f"Valor guardado para os limões: R$ {valor_guardado:.2f}")
print(f"Valor para cada amigo: R$ {valor_cada_amigo:.2f}")

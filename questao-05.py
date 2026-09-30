total_segundos = int(input("Digite o tempo total em segundos: "))

horas = total_segundos // 3600
resto = total_segundos % 3600

minutos = resto // 60
segundos = resto % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)

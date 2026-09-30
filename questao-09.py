distancia_km = float(input("Digite a distância percorrida em km: "))
tempo_minutos = float(input("Digite o tempo gasto em minutos: "))

tempo_horas = tempo_minutos / 60

velocidade_kmh = distancia_km / tempo_horas

distancia_metros = distancia_km * 1000
tempo_segundos = tempo_minutos * 60

velocidade_ms = distancia_metros / tempo_segundos

print(f"Velocidade média: {velocidade_kmh:.2f} km/h")
print(f"Velocidade média: {velocidade_ms:.2f} m/s")

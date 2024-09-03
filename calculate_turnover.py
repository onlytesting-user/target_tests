import json

with open('dados.json', 'r') as archive:
    turnover_by_month = json.load(archive)

def calculate_turnover(turnover_by_month):
    valid_turnover = [day['valor'] for day in turnover_by_month if day['valor'] > 0]

    lower_turnover = min(valid_turnover)
    higher_turnover = max(valid_turnover)

    monthly_average = sum(valid_turnover) / len(valid_turnover)

    days_above_average = len([valor for valor in valid_turnover if valor > monthly_average])

    return lower_turnover, higher_turnover, days_above_average

lower, higher, days_above_average = calculate_turnover(turnover_by_month)

print(f"Número de dias com faturamento acima da média mensal: {days_above_average} dias")
print(f"Maior valor de faturamento: R$ {higher:.2f}")
print(f"Menor valor de faturamento: R$ {lower:.2f}")

# Result:

# Número de dias com faturamento acima da média mensal: 10 dias
# Maior valor de faturamento: R$ 48924.24
# Menor valor de faturamento: R$ 373.78

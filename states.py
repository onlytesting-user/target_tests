turnover_by_states = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_turnover = sum(turnover_by_states.values())

for state, turnover in turnover_by_states.items():
    percentual = (turnover / total_turnover) * 100
    print(f"{state}: {percentual:.2f}%")

# Result:

# SP: 37.53%
# RJ: 20.29%
# MG: 16.17%
# ES: 15.03%
# Outros: 10.98%

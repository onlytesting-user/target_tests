sequence = input("Digite uma sequência de caracteres ou números: ")
final_sequence = ""

for character in sequence:
    final_sequence = character + final_sequence

# Exibe o resultado
print("Sequência original:", sequence)
print("Sequência invertida:", final_sequence)

# Result:

# Digite uma sequência de caracteres ou números: Bezerra
# Sequência original: Bezerra
# Sequência invertida: arrezeB

def belongs_to_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    if n == a or n == b:
        return True

    while b < n:
        a, b = b, a + b

    return b == n

number = int(input("Digite um número: "))

if belongs_to_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci!!")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci!!")

# Result:

# Digite um número: 20
# O número 20 não pertence à sequência de Fibonacci!!

# Digite um número: 21
# O número 21 pertence à sequência de Fibonacci!!

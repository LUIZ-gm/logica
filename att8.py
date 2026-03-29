import math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Potência, 6-Raiz, 7-Par, 8-Ímpar")
op = int(input("Escolha a operação: "))

if op == 1:
    print(f"Resultado: {n1 + n2}")
elif op == 2:
    print(f"Resultado: {n1 - n2}")
elif op == 3:
    print(f"Resultado: {n1 * n2}")
elif op == 4:
    print(f"Resultado: {n1 / n2}" if n2 != 0 else "Erro: Divisão por zero")
elif op == 5:
    print(f"Resultado: {n1 ** n2}")
elif op == 6:
    print(f"Raiz de {n1}: {math.sqrt(n1)} | Raiz de {n2}: {math.sqrt(n2)}")
elif op == 7:
    print(f"{n1} é par? {n1 % 2 == 0} | {n2} é par? {n2 % 2 == 0}")
elif op == 8:
    print(f"{n1} é ímpar? {n1 % 2 != 0} | {n2} é ímpar? {n2 % 2 != 0}")
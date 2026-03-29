n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

situacao = "APROVADO" if conceito in ["A", "B", "C"] else "REPROVADO"

print(f"\nNotas: {n1}, {n2}, {n3}, {n4}")
print(f"Média Final: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")
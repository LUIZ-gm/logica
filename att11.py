salario_atual = float(input("Digite o salário atual: R$ "))

if salario_atual <= 1000:
    percentual = 20
elif salario_atual <= 1700:
    percentual = 15
elif salario_atual <= 2300:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento

print(f"Salário digitado: R$ {salario_atual:.2f}")
print(f"Aumento         : {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário    : R$ {novo_salario:.2f}")
salario_bruto = float(input("Digite o salário bruto: R$ "))

# Cálculo simplificado INSS 2023
if salario_bruto <= 1302.00:
    inss = salario_bruto * 0.075
elif salario_bruto <= 2571.29:
    inss = salario_bruto * 0.09
elif salario_bruto <= 3856.94:
    inss = salario_bruto * 0.12
else:
    inss = salario_bruto * 0.14

salario_base_ir = salario_bruto - inss

# Cálculo IRRF 2023
if salario_base_ir <= 1903.98:
    irrf = 0
elif salario_base_ir <= 2826.65:
    irrf = (salario_base_ir * 0.075) - 142.80
elif salario_base_ir <= 3751.05:
    irrf = (salario_base_ir * 0.15) - 354.80
elif salario_base_ir <= 4664.68:
    irrf = (salario_base_ir * 0.225) - 636.13
else:
    irrf = (salario_base_ir * 0.275) - 869.36

print(f"INSS: R$ {inss:.2f}")
print(f"IRRF: R$ {irrf:.2f}")
print(f"Salário Líquido: R$ {salario_bruto - inss - irrf:.2f}")
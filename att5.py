peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (ex: 1.75): "))

imc = peso / (altura ** 2)

if imc < 16:
    classificacao = "Magreza grave"
elif imc < 17:
    classificacao = "Magreza moderada"
elif imc < 18.5:
    classificacao = "Magreza leve"
elif imc < 25:
    classificacao = "Saudável"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc < 40:
    classificacao = "Obesidade Grau II (severa)"
else:
    classificacao = "Obesidade Grau III (mórbida)"

print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")
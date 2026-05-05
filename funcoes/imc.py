# Calcular qual o IMC do usuário.

def imc(peso, altura):
    return peso / altura ** 2

peso = float(input("Digite o peso Kg: "))
altura = float(input("Digite a altura: "))

resultado = imc(peso, altura)
print(f"Seu IMC é {resultado:.2f}")

if resultado < 18:
    print("Abaixo do peso.")
elif resultado < 25:
    print("peso normal.")
elif resultado < 30:
    print("Sobrepeso.")
else:
    print("Obsidade.")

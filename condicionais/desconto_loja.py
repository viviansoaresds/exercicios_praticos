# Exercício 04: Verificar se está apto para receber o desconto

valor = float(input("Digite o valor da compra: R$ "))

if valor <= 100:
    desconto = 0
elif valor <= 200:
    desconto = 0.10
else: 
    desconto = 0.20

valor_final = valor - (valor * desconto)

print("/n----RESUMO DA COMPRA----")
print(f"Valor original: R$ {valor:.2f}")
print(f"Desconto {desconto * 100:.0f}%")
print(f"Valor final {valor_final:.2f}")
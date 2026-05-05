# Calcular quanto de troco o consumidor vai receber

def troco(total_compra, valor_pago):
    return valor_pago - total_compra

total_compra = float(input("Digite o valor total da compra: "))
valor_pago = float(input("Quanto você entregou R$: "))

resultado = troco(total_compra, valor_pago)

if resultado < 0:
    print("Valor insulficiente.")
else:
    print(f"Seu troco é {resultado:.2f}")

numeros = []
resposta = "s"

while resposta == "s":
    valor = int(input("Digite o valor: "))
    if valor not in numeros:
        numeros.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado, não vou adicionar...")
    resposta = (input("Quer continuar? s/n: "))

numeros.sort()
print(f"Você digitou os valores {numeros}")


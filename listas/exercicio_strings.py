# Exercício 4: Manipulação de lista de strings com slicing e ordenação

nomes = ["Vívian", "Alan", "Julia", "Vitória", "Ana"]
print(f"O primeiro: {nomes[0]}")
print(f"O último: {nomes[-1]}")

print("\nOrdem alfabética:")
for nome in sorted(nomes):
    print(nome)

print("\nAo contrário:")
for nome in nomes[::-1]:
    print(nome)

busca = input("Digite um nome: ")

if busca in nomes:
    posicao = nomes.index(busca)
    print(f"{busca} está na posição {posicao}")
else:
    print("Nome não encontrado.")
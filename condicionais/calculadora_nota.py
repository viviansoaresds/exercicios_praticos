# Exercício 03: Verificar se o aluno está aprovado ou reprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Parabéns, você está aprovado! Média final: {media:.2f}")
elif media >= 5 and media <= 6.9:
    print(f"Você está de recuperação! Média final: {media:.2f}")
elif media < 5:
    print(f"Você está reprovado. Média final: {media:.2f}")
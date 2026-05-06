# Exercício 03: Verificar se o aluno está aprovado ou reprovado

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def resultado(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media <= 6.9:
        return "Recuperação"
    elif media < 5:
        return "Reprovado"

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_final = media(nota1, nota2, nota3)
status = resultado(media_final)
print(f"{status}! Média final: {media_final:.2f}")




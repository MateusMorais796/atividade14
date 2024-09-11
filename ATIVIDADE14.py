# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

nota1 = float(input("Digite sua primeira nota "))
nota2 = float(input("Digite sua segunda nota "))
nota3 = float(input("Digite sua terceira nota "))

media = (nota1+nota2+nota3)/3

print(media)

if (media>=7):
    print("Você está aprovado")
elif (media>=5) and (media<7):
    print("Você está de recuperação")
elif (media<5):
    print("Você está reprovado")
"""
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
"""

a = float(input("infome a primeira nota escolar: "))
b = float(input("infome a segunda nota escolar: "))
c = float(input("infome a terceira nota escolar: "))
d = float(input("infome a quarta nota escolar: "))

media = (a + b + c + d) / 4

if (media >= 5):
    print("você foi aprovado")

else:
    print(f"você foi reprovado poissua média foi {media}")
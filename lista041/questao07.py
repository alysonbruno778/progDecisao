"""
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo
"""

num = int(input("Informe um valor positivo ou negativo: "))

if (num >= 1):
    print(f"O módulo do número é: {num}")

else:
    print(f"O módulo do número é: {num * (-1)}")


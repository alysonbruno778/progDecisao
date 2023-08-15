"""
Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido
"""

a = int(input("Informe um número inteiro: "))
b = int(input("Informe outro número inteiro: "))

if (a > b):
    print(f"A diferença de valores é de {a - b} ")

else:
    print(f"A diferença de valores é de {b - a}")
"""
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar
"""

a = int(input("Informe um número: "))

resto = a % 2
if ( resto == 0):
    print(f"O número {a} é par")

else:
    print(f"O número {a} impar")
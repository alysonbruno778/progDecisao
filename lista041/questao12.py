"""
Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número.
"""

a = int(input("Informe um número inteiro"))
b = int(input("Informe outro número inteiro"))
c = int(input("Informe outro número inteiro"))
d = int(input("Informe outro número inteiro"))
e = int(input("Informe outro número inteiro"))

maior = a

if ( maior < b ):
    maior = b

if ( maior < c ):
    maior = c

if ( maior < d ):
    maior = d

if ( maior < e ):
    maior = e

menor = a

if (menor < b):
    menor = b

if (menor < c):
    menor = c

if (menor < d):
    menor = d

if (menor < e):
    menor = e

print(f"O maior valor inserido foi {maior}")
print(f"O maior valor inserido foi {menor}")

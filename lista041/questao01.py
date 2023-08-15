"""
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações
"""

a = float(input("Informe um número: "))

if ( a > 20 ):
    b = a / 2
    print(f"A metade de {a} é {b}")

else:
    print(f"o número inserido foi {a}")
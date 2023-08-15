"""
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
"""

num = int(input("Informe um número inteiro: "))

if ( num <= 10 and num >= 1 ):
    print("Esse número está entre 1 e 10")

else:
    print("Esse número não está entre 1 e 10")
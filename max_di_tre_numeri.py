"""Massimo tra 3 numeri inseriti dall'utente"""
a = eval(input("Primo numero: "))
b = eval(input("Secondo numero: "))
c = eval(input("Terzo numero: "))

if a > b and a > c:
    massimo = a
else:
    if b > c:
        massimo = b
    else:
        massimo = c

print("Il massimo è:", massimo)
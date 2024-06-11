V = int(input())
A = int(input())
F = int(input())
P = int(input())

quantidade = 0

lista_dividas = [A, F, P]
lista_dividas.sort()

if (lista_dividas[0]) <= V:
    quantidade = 1

if (lista_dividas[0] + lista_dividas[1]) <= V:
    quantidade = 2

if (lista_dividas[0] + lista_dividas[1] + lista_dividas[2]) <= V:
    quantidade = 3

print(quantidade)
# n número de personas suscritas
# a número de suscriptores en línea
# q notificaciones de si se conecta o desconecta un suscriptor + si se conecta, - en caso contrario
# al principio a < n, si a logra, despues de las notificaciones(+ , -), o entre medio, ser igual que n es yes, si no es no, y si no se sabe es maybe

t = int(input())

for _ in range(t):
    n, a, q = map(int, input().split())
    suscriptores = a
    q = int(q)
    for _ in range(q):
        x = input()
        if x == "+":
            suscriptores += 1
        elif x == "-":
            suscriptores = max(0, suscriptores-1)
        else:
            print("error")
    if suscriptores == n:
        print("Yes")
    else:
        if suscriptores > a or suscriptores > 0:
            print("Maybe")
        else:
            print("No")

# n número de personas suscritas
# a número de suscriptores en línea
# q notificaciones de si se conecta o desconecta un suscriptor + si se conecta, - en caso contrario
# al principio a < n, si a logra, despues de las notificaciones(+ , -), o entre medio, ser igual que n es yes, si no es no, y si no se sabe es maybe

t = int(input())

for _ in range(t):
    n, a, q = map(int, input().split())
    a = int(a)
    q = int(q)
    for _ in range(q):
        x = input()
        if x == "+":
            a += 1
        elif x == "-":
            a -= 1
        else:
            print("error")
    if a == n:
        print("Yes")
    elif a < n:
        print("No")
    else:
        print("Maybe")

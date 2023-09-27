n = int(input())

a = [*map(int, input().split())]
m = abs(a[0])

for x in a[1:]:
    if abs(x) < m:
        m = abs(x)

print(m)
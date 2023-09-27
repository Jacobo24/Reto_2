from math import ceil
t = int(input())
for _ in range(t):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = abs(a - b)
    print(ceil(d//(2*c)))
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    length = y - x
    for i in range(1, 100000000):
        if length <= (i**2):
            n = i
            break
    k = 2*n - 1
    if n**2 - (n - 1) <= length <= n**2:
        print(k)
    else:
        print(k-1)
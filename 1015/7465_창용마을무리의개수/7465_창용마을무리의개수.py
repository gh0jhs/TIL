def find(x):
    if p[x] == x:
        return x
    else:
        return find(p[x])

def union(x, y):
    p[find(y)] = find(x)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    p = list(range(n + 1))
    for i in range(len(arr)):
        x, y = arr[i][0], arr[i][1]
        union(x, y)
    for i in range(1,len(p)):
        p[i] = find(i)
    print('#{} {}'.format(tc,len(set(p[1:]))))
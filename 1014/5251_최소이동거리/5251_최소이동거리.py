import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] == x:
        return x
    else:
        return find(p[x])

def union(x, y):
    p[find(y)] = find(x)


T = int(input())
for tc in range(1, T+1):
    answer = []
    n, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]
    arr.sort(key=lambda x: x[2])
    p = list(range(n+1))

    cnt = 0
    for i in range(len(arr)):
        a, b, c = arr[i][0], arr[i][1], arr[i][2]
        if find(a) != find(b):
            union(a, b)
            answer.append([[a,b], c])
            cnt += 1
        if cnt == n:
            break
    answer.sort()
    print(answer)

    visited = [0 for _ in range(n+1)]
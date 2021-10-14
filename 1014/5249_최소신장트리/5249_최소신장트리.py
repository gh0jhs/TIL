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
    v, e = map(int, input().split()) # v: 마지막 번호, e: 간선의 개수
    visited = [0 for _ in range(e+1)]
    arr = [list(map(int, input().split())) for _ in range(e)]
    arr.sort(key=lambda x: x[2])
    p = list(range(v+1))

    answer = 0
    cnt = 0
    for i in range(len(arr)):
        a, b, c = arr[i][0], arr[i][1], arr[i][2]
        if find(a) != find(b):
            union(a, b)
            answer += c
            cnt += 1
        if cnt == v:
            break
    print('#{} {}'.format(tc, answer))
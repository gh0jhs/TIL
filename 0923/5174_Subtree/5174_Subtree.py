import sys
sys.stdin = open('input.txt')

def dfs(n):
    global cnt
    cnt += 1
    visited[n] = 1

    for i in range(len(data)):
        if data[n][i] == 1 and visited[i] == 0:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))

    visited = [0 for _ in range(e+2)]
    data = [[0 for _ in range(e+2)] for _ in range(e+2)]

    for i in range(0, len(arr)-1, 2):
        data[arr[i]][arr[i+1]] = 1

    cnt = 0
    dfs(n)
    print('#{} {}'.format(tc, cnt))
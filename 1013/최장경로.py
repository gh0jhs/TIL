import sys
sys.stdin = open('input.txt')

def dfs(v, cnt):
    global answer
    answer = max(answer, cnt)
    visited[v] = 1
    for w in range(len(arr)):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w, cnt+1)
    visited[v] = 0


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    answer = 0
    cnt = 1
    if m == 0:
        answer = 1
    else:
        data = [list(map(int, input().split())) for _ in range(m)]
        arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
        visited = [0 for _ in range(n+1)]
        # print(data)

        for i in range(len(data)):
            x, y = data[i][0], data[i][1]
            arr[x][y], arr[y][x] = 1, 1
        # print(arr)
        lst = []
        for i in range(1, n+1):
            dfs(i, cnt)
    print('#{} {}'.format(tc, answer))

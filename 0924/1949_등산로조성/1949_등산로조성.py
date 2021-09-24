import sys
sys.stdin = open('input.txt')

def dfs(x, y, cnt):
    global chance, ans
    ans = max(ans, cnt)

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] < arr[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = 0

            for i in range(1, k+1):
                if arr[nx][ny] - i < arr[x][y] and visited[nx][ny] == 0 and chance == False:
                    chance = True
                    arr[nx][ny] -= i
                    visited[nx][ny] = 1
                    dfs(nx, ny, cnt+1)
                    chance = False
                    arr[nx][ny] += i
                    visited[nx][ny] = 0


T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_temp = -100
    for i in range(n):
        if max_temp < max(arr[i]):
            max_temp = max(arr[i])

    max_lst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_temp:
                max_lst.append([i, j])
    # print(max_lst)
    max_len = []
    for i in range(len(max_lst)):
        visited = [[0 for _ in range(n)] for _ in range(n)]
        chance = False
        ans = 0
        visited[max_lst[i][0]][max_lst[i][1]] = 1
        dfs(max_lst[i][0], max_lst[i][1], 1)
        max_len.append(ans)
        # print(max_len)
    print('#{} {}'.format(tc, max(max_len)))
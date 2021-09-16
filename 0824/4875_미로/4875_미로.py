import sys
sys.stdin = open('input.txt')
#
# fail
def dfs(x, y):
    global visited
    visited[x][y] = 1
    # 우 하 좌 상
    dx = [1, 0, -1 ,0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        if x == 0:
            if i == 2:
                continue
        elif x == n-1:
            if i == 0:
                continue
        if y == 0:
            if i == 3:
                continue
        elif y == n-1:
            if i == 1:
                continue
        nx = x + dx[i]
        ny = y + dy[i]
        if (arr[nx][ny] == 0 or arr[nx][ny] == 3) and visited[nx][ny] == 0:
            dfs(nx, ny)


T = int(input())
for tc in range(1, T+1):
    s = (0, 0)
    n = int(input())
    arr = [list(map(int, (map(str, input())))) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                s = (i, j)
            if arr[i][j] == 3:
                e = (i, j)
    dfs(s[0], s[1])
    if visited[e[0]][e[1]] == 1:
        result = 1
    else:
        result = 0
    print(visited)
    print('#{} {}'.format(tc, result))
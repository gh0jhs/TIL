import sys
sys.setrecursionlimit(100000)

def check(x, y):
    if 0 <= x < n and 0 <= y < n and visited[x][y] == 0:
        return True
    return False

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if check(nx, ny):
            if arr[x][y] == arr[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny)
                
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
visited = [[0]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt2 += 1
print(cnt, cnt2)
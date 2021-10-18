def bfs(x, y):
    que.append([x, y])
    while que:
        q = que.pop(0)
        x, y = q[0], q[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= size and visited[nx][ny] == 0:
                que.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if 0 < arr[nx][ny] < size:
                    fish.append([visited[nx][ny], nx, ny])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
cnt = 0
size = 2
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sx, sy = i, j
            break
arr[sx][sy]  = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while True:
    que = []
    fish = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    bfs(sx, sy)
    if fish == []:
        break
    fish.sort()
    answer += fish[0][0]
    sx, sy = fish[0][1], fish[0][2]
    arr[sx][sy] = 0
    cnt += 1 
    if cnt == size:
        size += 1
        cnt = 0
print(answer)
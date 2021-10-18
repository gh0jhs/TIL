from collections import deque
import copy

def recur(cur, start):
    if cur == m:
        temp = lst[:]
        CC.append(temp)
        return

    for i in range(start, len(C)):
        lst[cur] = C[i]
        recur(cur+1, i+1)

def bfs(x, y):
    global temp2
    que.append([x, y])
    visited[x][y] = 1

    while que:
        q = que.popleft()
        x, y = q[0], q[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                que.append([nx, ny])
                if data[nx][ny] == 2:
                    temp2 += visited[x][y]
                    que.clear()
                    return
                visited[nx][ny] = visited[x][y] + 1

                if visited[nx][ny] >= answer:
                    temp2 += visited[nx][ny]
                    return

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 1500
que = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
C = []
CC = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            C.append([i, j])
            arr[i][j] = 0
lst = [0] * m
recur(0, 0)


for i in range(len(CC)):
    data = copy.deepcopy(arr)
    temp2 = 0
    for j in range(len(CC[i])):
        x, y = CC[i][j][0], CC[i][j][1]
        data[x][y] = 2
    for a in range(len(data)):
        for b in range(len(data[a])):
            if data[a][b] == 1:
                visited = [[0 for _ in range(n)] for _ in range(n)]
                bfs(a, b)
                if temp2 >= answer:
                    break
        if temp2 >= answer:
            break
    if answer > temp2:
        answer = temp2
print(answer)
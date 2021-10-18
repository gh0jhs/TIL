from collections import deque
import copy
def bfs(x, y):
    que.append([x, y])
    while que:
        q = que.popleft()
        for i in range(4):
            nx = q[0] + dx[i]
            ny = q[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                que.append([nx, ny])

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
que = deque()
answer = 0
lst = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            lst.append([i, j])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            arr = copy.deepcopy(data)
            if arr[lst[i][0]][lst[i][1]] == 0:
                arr[lst[i][0]][lst[i][1]] = 1
            else:
                continue
            if arr[lst[j][0]][lst[j][1]] == 0:
                arr[lst[j][0]][lst[j][1]] = 1
            else:
                continue
            if arr[lst[k][0]][lst[k][1]] == 0:
                arr[lst[k][0]][lst[k][1]] = 1
            else:
                continue
            for a in range(len(arr)):
                for b in range(len(arr[a])):
                    if arr[a][b] == 2:
                        bfs(a, b)
            max_temp = 0
            for c in range(len(arr)):
                for d in range(len(arr[c])):
                    if arr[c][d] == 0:
                        max_temp += 1
            if answer < max_temp:
                answer = max_temp
print(answer)
            
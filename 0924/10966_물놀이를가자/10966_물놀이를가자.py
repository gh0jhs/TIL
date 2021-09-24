import sys
sys.stdin = open('input.txt')

from collections import deque


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    visited = [[987654321 for _ in range(m)] for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # print(queue)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            if arr[nx][ny] == 'L' and visited[nx][ny] == 987654321:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += visited[i][j]
    print('#{} {}'.format(tc, ans))

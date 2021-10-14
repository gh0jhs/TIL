import sys
sys.stdin = open('input.txt')

from collections import deque



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[123456789 for _ in range(n)] for _ in range(n)]
    que = deque()
    que.append([0, 0])
    visited[0][0] = 0
    while que:
        q = que.popleft()
        x, y = q[0], q[1]

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                diff = 0
                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]

                if visited[nx][ny] > visited[x][y] + diff + 1:
                    visited[nx][ny] = visited[x][y] + diff + 1
                    que.append([nx, ny])

    answer = visited[n-1][n-1]
    print('#{} {}'.format(tc, answer))
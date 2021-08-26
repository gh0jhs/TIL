import sys
sys.stdin = open('input.txt')


def check(x, y):
    if x < 0 or n-1 < x or y < 0 or n-1 < y or arr[x][y] == '1' or arr[x][y] == '2':
        return False
    return True

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if check(nx, ny):
            if arr[nx][ny] == '3':
                return 1

            arr[nx][ny] = '1'
            if dfs(nx, ny):
                cnt += 1
                return cnt
    return 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                x = i
                y = j
    cnt = 0
    print('#{} {}'.format(tc, dfs(x, y)))

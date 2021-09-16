import sys
sys.stdin = open('input.txt')
#
def check(x, y):
    if x < 0 or 15 < x or y < 0 or 15 < y or arr[x][y] == '1' or arr[x][y] == '2':
        return False
    return True

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check(nx, ny):
            if arr[nx][ny] == '3':
                return 1
            arr[nx][ny] = '1'
            if dfs(nx, ny):
                return 1
    return 0

for tc in range(1, 11):
    test_case = int(input())
    arr = [list(input()) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                x = i
                y = j
    print('#{} {}'.format(tc, dfs(x, y)))
n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# top, up, left, right, down ,bot
p  = [1, 2, 4, 3, 5, 6]
for i in order:
    x += dx[i-1]
    y += dy[i-1]

    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[i-1]
        y -= dy[i-1]
        continue

# top, up, left, right, down ,bot

#  0 ,  1,   2,    3,     4,   5
    if i == 1:
        p[0], p[1], p[2], p[3], p[4], p[5] = p[2], p[1], p[5], p[0], p[4], p[3]
        if arr[x][y] == 0:
            arr[x][y] = dice[p[5]]
        else:
            dice[p[5]] = arr[x][y]
            arr[x][y] = 0
    elif i == 2:
        p[0], p[1], p[2], p[3], p[4], p[5] = p[3], p[1], p[0], p[5], p[4], p[2]
        if arr[x][y] == 0:
            arr[x][y] = dice[p[5]]
        else:
            dice[p[5]] = arr[x][y]
            arr[x][y] = 0
    elif i == 3:
        p[0], p[1], p[2], p[3], p[4], p[5] = p[4], p[0], p[2], p[3], p[5], p[1]
        if arr[x][y] == 0:
            arr[x][y] = dice[p[5]]
        else:
            dice[p[5]] = arr[x][y]
            arr[x][y] = 0
    elif i == 4:
        p[0], p[1], p[2], p[3], p[4], p[5] = p[1], p[5], p[2], p[3], p[0], p[4]
        if arr[x][y] == 0:
            arr[x][y] = dice[p[5]]
        else:
            dice[p[5]] = arr[x][y]
            arr[x][y] = 0
    print(dice[p[0]])

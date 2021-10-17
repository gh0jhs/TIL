import copy

def c1(x, y, r):
    nx = x
    ny = y
    while True:
        nx += dx[r]
        ny += dy[r]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 6:
            break
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'

def c2(x, y, r):
    if r == 0: # 상하
        c1(x, y, 0)
        c1(x, y, 2)
    elif r == 1:
        c1(x, y, 1)
        c1(x, y, 3)

def c3(x, y, r):
    if r == 0:
        c1(x, y, 1)
        c1(x, y, 2)
    elif r == 1:
        c1(x, y, 2)
        c1(x, y, 3)
    elif r == 2:
        c1(x, y, 3)
        c1(x, y, 0)
    elif r == 3:
        c1(x, y, 0)
        c1(x, y, 1)

def c4(x, y, r):
    if r == 0:
        c1(x, y, 1)
        c1(x, y, 2)
        c1(x, y, 3)
    elif r == 1:
        c1(x, y, 0)
        c1(x, y, 2)
        c1(x, y, 3)
    elif r == 2:
        c1(x, y, 0)
        c1(x, y, 1)
        c1(x, y, 3)
    elif r == 3:
        c1(x, y, 0)
        c1(x, y, 1)
        c1(x, y, 2)
def c5(x, y):
    c1(x, y, 0)
    c1(x, y, 1)
    c1(x, y, 2)
    c1(x, y, 3)

def recur(cur, n):
    if cur == n:
        temp = lst[:]
        lst_list.append(temp)
        return

    for i in range(4):
        lst[cur] = i
        recur(cur+1, n)

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 123456789

cam = []
cam5 = []
for i in range(n):
    for j in range(m):
        if str(data[i][j]) in '1234':
            cam.append([i, j, data[i][j]])
        if data[i][j] == 5:
            cam5.append([i, j])

lst = [0] * len(cam)
lst_list = []
recur(0, len(cam))
# print(lst_list)
# print(cam)
for i in range(len(lst_list)):
    arr = copy.deepcopy(data)
    temp = 0
    for j in range(len(lst_list[i])):
        x, y, num = cam[j][0], cam[j][1], cam[j][2]
        if num == 1:
            c1(x, y, lst_list[i][j])
        elif num == 2:
            c2(x, y, lst_list[i][j])
        elif num == 3:
            c3(x, y, lst_list[i][j])
        elif num == 4:
            c4(x, y, lst_list[i][j])
    for k in range(len(cam5)):
        x, y = cam5[k][0], cam5[k][1]
        c5(x, y)
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0:
                temp += 1
    if answer > temp:
        answer = temp
print(answer)
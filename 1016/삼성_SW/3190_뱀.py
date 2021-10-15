n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
direct_info = [list(input().split()) for _ in range(l)]
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(len(apple)):
    x, y = apple[i][0] - 1, apple[i][1] - 1
    arr[x][y] = 123456789

head = [0, 0]
tail = [0, 0]
direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direct_list = []

i = 0
cnt = 0
body = 1
while True:
    cnt += 1
    direct_list.append(i)
    head[0] += direct[i][0]
    head[1] += direct[i][1]

    if head[0] == -1 or head[0] == n or head[1] == -1 or head[1] == n:
        break

    if arr[head[0]][head[1]] == 1:
        break

    if arr[head[0]][head[1]] == 123456789:
        body += 1
        arr[head[0]][head[1]] = 1
        arr[tail[0]][tail[1]] = 1
    else:
        arr[head[0]][head[1]] = 1
        arr[tail[0]][tail[1]] = 0
        idx = direct_list[cnt - body]
        tail[0] += direct[idx][0]
        tail[1] += direct[idx][1]

    for k in range(len(direct_info)):
        if cnt == int(direct_info[k][0]):
            if direct_info[k][1] == 'D':
                i += 1
                if i == 4:
                    i = 0
            elif direct_info[k][1] == 'L':
                i -= 1
                if i == -1:
                    i = 3
print(cnt)

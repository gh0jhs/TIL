def dfs(x, y, cnt, temp):
    visited[x][y] = 1
    global answer
    answer = max(answer, temp)
    if cnt == 4:
        return
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            temp += arr[nx][ny]
            dfs(nx, ny, cnt+1, temp)
            visited[nx][ny] = 0
            temp -= arr[nx][ny]
    visited[x][y] = 0

def extra():
    global temp
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp1_1 = temp1_2 = temp1_3 = temp1_4 = 0
            # 1_1
            if 0 < i < n and 0 < j < m-1:
                temp1_1 = arr[i-1][j] + arr[i][j-1] + arr[i][j] + arr[i][j+1]
            # 1_2
            if 0 <= i < n-1 and 0 < j < m-1:
                temp1_2 = arr[i+1][j] + arr[i][j-1] + arr[i][j] + arr[i][j+1]
            # 1_3
            if 0 < i < n-1 and 0 <= j < m-1:
                temp1_3 = arr[i-1][j] + arr[i][j] + arr[i+1][j] + arr[i][j+1]
            # 1_4
            if 0 < i < n-1 and 0 < j < m:
                temp1_4 = arr[i][j-1] + arr[i][j] + arr[i-1][j] + arr[i+1][j]
            temp = max(temp1_1, temp1_2, temp1_3, temp1_4, temp)
        

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
temp = 0

visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        dfs(i, j, 1, arr[i][j])
extra()
answer = max(answer, temp)
print(answer)
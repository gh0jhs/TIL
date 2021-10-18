def find(x):
    if p[x] == x:
        return x
    else:
        return find(p[x])

def union(x, y):
    p[find(y)] = find(x)

n, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while True:
    lst = []
    p = list(range(n**2))
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if L <= abs(arr[i][j] - arr[nx][ny]) <= R:
                        lst.append([n*i+j, n*nx+ny])
    if lst == []:
        break
    for i in range(len(lst)):
        x, y = lst[i][0], lst[i][1]
        if find(x) != find(y):
            union(x, y)
    
    for i in range(len(p)):
        p[i] = find(i)

    A = [0 for _ in range(n**2)]
    B = [0 for _ in range(n**2)]
    C = [0 for _ in range(n**2)]
    for i in range(n):
        for j in range(n):
            A[find(n*i+j)] += arr[i][j]
            B[find(n*i+j)] += 1
    for i in range(len(C)):
        if B[i] != 0:
            C[i] = A[i] // B[i]
    for i in range(n):
        for j in range(n):
            arr[i][j] = C[find(n*i+j)]
    answer += 1
print(answer)
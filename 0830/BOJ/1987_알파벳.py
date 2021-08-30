# 정답
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [arr[0][0]]
answer = 1
def check(x, y):
    if 0<=x<R and 0<=y<C and arr[x][y] not in visited:
        return True
    return False

def dfs(x, y, cnt):
    global answer

    answer = max(answer, cnt)

    dx = [0, 0, -1 ,1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if check(nx,ny):
            visited.append(arr[nx][ny])
            dfs(nx, ny, cnt+1)
            visited.pop()
dfs(0,0,answer)
print(answer)

# 내가 한 것
# R, C = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
# visited = [arr[0][0]]
# cnt = 1

# def check(x, y):
#     if 0<=x<R and 0<=y<C and arr[x][y] not in visited:
#         return True
#     return False


# def dfs(x, y):
#     global cnt
#     dx = [0, 0, -1 ,1]
#     dy = [1, -1, 0, 0]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if check(nx,ny):
#             visited.append(arr[nx][ny])
#             ###
#             if dfs(nx,ny):
#                 cnt += 1
#                 return cnt
#     return 0
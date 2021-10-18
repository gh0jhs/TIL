from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = list(combinations(list(range(n)), n//2))
length = len(lst)
start = lst[:length//2]
link = lst[length//2:][::-1]
ans = 123456789

for i in range(len(start)):
    A = list(combinations(start[i], 2))
    B = list(combinations(link[i], 2))
    ans_A = 0
    ans_B = 0
    for j in range(len(A)):
        x, y = A[j][0], A[j][1]
        u, v = B[j][0], B[j][1]
        ans_A += arr[x][y] + arr[y][x]
        ans_B += arr[u][v] + arr[v][u]
    ans = min(abs(ans_A - ans_B), ans)
print(ans)
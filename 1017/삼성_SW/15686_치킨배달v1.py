def recur(cur, start):
    if cur == m:
        temp = lst[:]
        CC.append(temp)
        return

    for i in range(start, len(C)):
        lst[cur] = C[i]
        recur(cur+1, i+1)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

A = []
AA = []
AAA = []
C = []
CC = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            C.append([i, j])
        elif arr[i][j] == 1:
            A.append([i, j])
lst = [0] * m
recur(0, 0)

for i in range(len(CC)):
    for k in range(len(A)):
        temp = 10000
        a, b = A[k][0], A[k][1]
        for j in range(len(CC[i])):
            x, y = CC[i][j][0], CC[i][j][1]
            temp = min(abs(a-x) + abs(b-y), temp)
        AA.append(temp)
    AAA.append(AA)
    AA = []

answer = 100000
for i in range(len(AAA)):
    answer = min(sum(AAA[i]), answer)
print(answer)
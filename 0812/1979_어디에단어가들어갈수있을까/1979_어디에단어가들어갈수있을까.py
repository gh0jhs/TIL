import sys
sys.stdin = open('input.txt')
#
tc = int(input())
result = []
for _ in range(tc):
    val = 0
    arr = []
    n, k = map(int, input().split())
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 0:
                cnt = 0
            elif arr[i][j] == 1:
                cnt += 1
            if cnt == k:
                if j == n-1:
                    val += 1
                elif arr[i][j+1] == 0:
                    val += 1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 0:
                cnt = 0
            elif arr[j][i] == 1:
                cnt += 1
            if cnt == k:
                if j == n-1:
                    val += 1
                elif arr[j+1][i] == 0:
                    val += 1

    result.append(val)
for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))
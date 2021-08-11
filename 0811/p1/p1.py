import sys
sys.stdin = open('input.txt')

tc = int(input())
result = []
result2 = []
for _ in range(tc):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            if j > 0:
                temp += abs(arr[i][j] - arr[i][j-1])
            if j < n-1:
                temp += abs(arr[i][j]  - arr[i][j+1])
            if i > 0:
                temp += abs(arr[i][j] - arr[i-1][j])
            if i < n-1:
                temp += abs(arr[i][j] - arr[i+1][j])
            result.append(temp)
    result2.append(sum(result))
    result = []
for i in range(tc):
    print('#{} {}'.format(i+1, result2[i]))
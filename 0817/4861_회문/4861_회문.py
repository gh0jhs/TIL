import sys
sys.stdin = open('input.txt')

result = []
T = int(input())
for _ in range(T):
    n, m = map(int, input().split()) # 입력


    arr = []
    for _ in range(n):
        arr.append(list(input())) # 입력 리스트로..

# 가로
    for i in range(n):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m//2):
                if arr[i][k+j] == arr[i][m-k-1+j]:
                    cnt += 1
            if cnt == m//2:
                temp = ''
                for l in range(m):
                    temp += arr[i][j+l]
                result.append(temp)

# 세로
    for i in range(n):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m//2):
                if arr[k+j][i] == arr[m-k-1+j][i]:
                    cnt += 1
            if cnt == m//2:
                temp = ''
                for l in range(m):
                    temp += arr[j+l][i]
                result.append(temp)

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))
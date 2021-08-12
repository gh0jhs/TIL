import sys
sys.stdin = open('input.txt')

tc = int(input())
result = []
for _ in range (tc):
    n = int(input())
    lst = [] # list 초기화
    cnt = 0 # 3의 갯수 초기화
    arr = [[0 for col in range(10)] for row in range(10)] # 100*100 크기의 0원소로 초기화

    for _ in range(n):
        lst.append(list(map(int, input().split()))) # 인풋

    for i in lst:
        if i[4] == 1: # 빨간색
            for j in range(i[0], i[2]+1):
                for k in range(i[1], i[3]+1):
                    if arr[j][k] == 2: # 2로 채워져있으면 3대입
                        arr[j][k] = 3
                    elif arr[j][k] == 0 or 1: # 2로 채워져있지 않으면 1대입
                        arr[j][k] = 1

        elif i[4] == 2: # 파란색
            for j in range(i[0], i[2]+1):
                for k in range(i[1], i[3]+1):
                    if arr[j][k] == 1:
                        arr[j][k] = 3
                    elif arr[j][k] == 0 or 2:
                        arr[j][k] = 2

    for i in arr:   # arr 원소3 갯수 새기
        for j in i:
            if j == 3:
                cnt += 1
    result.append(cnt)

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))

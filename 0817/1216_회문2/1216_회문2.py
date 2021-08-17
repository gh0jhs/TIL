import sys
sys.stdin = open('input.txt')

result = []
for _ in range(10):
    arr = []
    tc = int(input())
    for _ in range(100):
        arr.append(list(input())) # 초기화와 입력 받는 과정

    arr_r = list(map(list, zip(*arr)))

    max_temp = 1
    for k in range(100):
        for i in range(99, -1, -1):
            for j in range(100-i+1):
                temp1 = arr[k][j:j+i]
                temp2 = temp1[::-1]
                if temp1 == temp2:
                    if max_temp < len(temp1):
                        max_temp = len(temp1)
    for k in range(100):
        for i in range(99, -1, -1):
            for j in range(100-i+1):
                temp1 = arr_r[k][j:j+i]
                temp2 = temp1[::-1]
                if temp1 == temp2:
                    if max_temp < len(temp1):
                        max_temp = len(temp1)

    result.append(max_temp)
for i in range(10):
    print('#{} {}'.format(i+1, result[i]))

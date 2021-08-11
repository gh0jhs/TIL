import sys
sys.stdin = open('input.txt')

result = []
tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = [[0 for col in range(n)] for row in range(n)]

    cnt = 0
    i = 0
    j = -1
    cnt_move = 0
    cnt_2 = 0
    dir = 1
    temp = n - 1

    for _ in range(n):
        j += 1
        cnt += 1
        arr[i][j] = cnt

    while cnt != n**2:
        cnt += 1
        if dir % 4 == 0:
            j += 1
            arr[i][j] = cnt
            if cnt_move == temp:
                temp -= 1
                cnt_2 += 1
                cnt_move = 0
                if cnt_2 == 1:
                    cnt_2 = 0
                    dir += 1
        elif dir % 4 == 1:
            i += 1
            arr[i][j] = cnt
            cnt_move += 1
            if cnt_move == temp:
                temp -= 1
                cnt_2 += 1
                cnt_move = 0
                if cnt_2 == 1:
                    cnt_2 = 0
                    dir += 1
        elif dir % 4 == 2:
            j -= 1
            arr[i][j] = cnt
            if cnt_move == temp:
                temp -= 1
                cnt_2 += 1
                cnt_move = 0
                if cnt_2 == 1:
                    cnt_2 = 0
                    dir += 1
        elif dir % 4 == 3:
            i -= 1
            arr[i][j] = cnt
            if cnt_move == temp:
                temp -= 1
                cnt_2 += 1
                cnt_move = 0
                if cnt_2 == 1:
                    cnt_2 = 0
                    dir += 1
    result.append(arr)
for i in range(tc):
    print('#{}'.format(i+1))
    for j in arr[i]:
        print(*j)


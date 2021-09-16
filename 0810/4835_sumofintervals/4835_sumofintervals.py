import sys
sys.stdin = open('input.txt')
#
result = []
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    lst = []

    lst.extend(list(map(int, input().split())))
    min_val = 1000000
    max_val = 0
    for i in range(-1, len(lst)):
        cnt = 0
        temp = 0
        for j in range(i+1, len(lst)):
            temp += lst[j]
            cnt += 1
            if cnt == m:
                if min_val > temp:
                    min_val = temp
                if max_val < temp:
                    max_val = temp
    result.append(max_val - min_val)
for i in range(T):
    print('#{} {}'.format(i+1, result[i]))
    0
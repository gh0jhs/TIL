import sys
sys.stdin = open('input.txt')
#
tc = int(input())
result = []

for _ in range(tc):
    arr = []
    n, m = map(int, input().split())
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    max_val = 0
    for i in range(n):
        for j in range(n):
            temp = 0
            if i+m <= n and j+m <= n:
                for k in range(i, i+m):
                    for l in range(j, j+m):
                        temp += arr[k][l]
                        if temp > max_val:
                            max_val = temp
    result.append(max_val)
for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))
import sys
sys.stdin = open('input.txt')

result = []
tc = int(input())
for _ in range(tc):
    arr = []
    for _ in range(5):
        arr.append(list(input()))
    max_len = len(arr[0])
    for i in range(len(arr)):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    for i in range(len(arr)):
        x = max_len - len(arr[i])
        for _ in range(x):
            arr[i].append('')
    arr_r = list(map(list, zip(*arr)))
    s = ''
    for i in range(len(arr_r)):
        for j in range(len(arr_r[i])):
            s += arr_r[i][j]
    result.append(s)

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))
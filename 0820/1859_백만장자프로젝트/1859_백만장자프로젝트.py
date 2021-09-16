import sys
sys.stdin = open('input.txt')
#
result = []
tc = int(input())
for _ in range(tc):
    total = 0
    n = int(input())
    arr = list(map(int, input().split()))
    while True:
        max_idx = arr.index(max(arr))
        for i in range(max_idx):
            total += arr[max_idx] - arr[i]
        if max_idx == len(arr) - 1:
            break
        arr = arr[max_idx+1:]
    result.append(total)

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))

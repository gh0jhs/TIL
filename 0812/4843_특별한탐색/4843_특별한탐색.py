import sys
sys.stdin = open('input.txt')

T = int(input())
result = []


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        idx = i
        for j in range(i+1, N):
            if i%2 == 1:
                if arr[idx] > arr[j]:
                    idx = j
            else:
                if arr[idx] < arr[j]:
                    idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()

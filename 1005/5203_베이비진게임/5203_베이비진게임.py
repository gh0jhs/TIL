import sys
sys.stdin = open('input.txt')

def babygin(arr):
    arr.sort()
    # triplet
    for i in range(len(arr)):
        if arr.count(arr[i]) >= 3:
            return True

    # run
    arr = list(set(arr)) # 중복 제거
    run = 1
    temp = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - temp == 1:
            run += 1
        else:
            run = 1
        if run >= 3:
            return True
        temp = arr[i]


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    A = []
    B = []
    ans = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            A.append(arr[i])
        else:
            B.append(arr[i])

        if i >= 4:
            if babygin(A):
                ans = 1
                break
        if i >= 5:
            if babygin(B):
                ans = 2
                break

    print('#{} {}'.format(tc, ans))
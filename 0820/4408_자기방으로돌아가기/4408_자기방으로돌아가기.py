import sys
sys.stdin = open('input.txt')
#
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    room = [0 for _ in range(401)]

    for i in range(len(arr)):
        if arr[i][0] <= arr[i][1]:
            for j in range(arr[i][0], arr[i][1]+1):
                room[j] += 1
        else:
            for j in range(arr[i][0], arr[i][1]-1, -1):
                room[j] += 1

    print('#{} {}'.format(tc, max(room)))

    # 9 / 10 fail
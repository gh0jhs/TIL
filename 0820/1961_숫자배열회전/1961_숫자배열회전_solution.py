import sys
sys.stdin = open('input.txt')

def rotate(arr):
    newArr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newArr[j][N-1-i] = arr[i][j]
    return newArr

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = rotate(arr)
    b = rotate(a)
    c = rotate(b)

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, a[i])), ''.join(map(str, b[i])), ''.join(map(str, c[i])))
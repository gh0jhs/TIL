import sys
sys.stdin = open('input.txt')

def inorder(v):
    if v:
        inorder(left[v])
        print(data[v], end='')
        inorder(right[v])

for tc in range(1, 11):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    data = ['' for _ in range(n+1)]
    left = [0 for _ in range(n+1)]
    right = [0 for _ in range(n+1)]
    for i in range(len(arr)):
        x = int(arr[i][0])
        data[x] = arr[i][1]
        if len(arr[i]) == 3:
            left[x] = int(arr[i][2])
        elif len(arr[i]) == 4:
            left[x] = int(arr[i][2])
            right[x] = int(arr[i][3])
    print('#{} '.format(tc), end='')
    inorder(1)
    print()

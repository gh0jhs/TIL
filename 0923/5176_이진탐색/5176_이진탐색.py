import sys
sys.stdin = open('input.txt')

def inorder(v):
    global x
    if 2 * v <= n:
        if arr[2*v] == 0:
            inorder(2*v)

    if arr[v] == 0:
        arr[v] = x
        x += 1

    if 2 * v + 1 <= n:
        if arr[2*v + 1] == 0:
            inorder(2*v + 1)

T = int(input())
for tc in range(1, T+1):
    x = 1
    n = int(input())
    arr = [0 for _ in range(n+1)]
    inorder(1)
    print(arr)
    print('#{} {} {}'.format(tc, arr[1], arr[n//2]))
import sys
sys.stdin = open('input.txt')

result = []
for _ in range(10):
    arr = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0 for _ in range(100)]
    tc, n = map(int, input().split())
    lst = list(map(int, input().split()))
    x1 = x2 = 0
    for i in range(len(lst)):
        if i%2 == 0:
            x1 = lst[i]
        else:
            x2 = lst[i]
            arr[x1][x2] = 1

    stack = [0]
    top = 0
    visited[0] = 1
    i = 0
    while top != -1:
        for j in range(100):
            if arr[i][j] == 1 and visited[j] == 0:
                stack.append(j)
                top += 1
                visited[j] = 1
                i = j
        else:
            top -= 1
            i = stack[top]

    if 99 in stack:
        result.append(1)
    else:
        result.append(0)
for i in range(10):
    print('#{} {}'.format(i+1, result[i]))
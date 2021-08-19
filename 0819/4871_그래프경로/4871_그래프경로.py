import sys
sys.stdin = open('input.txt')

result = []
tc = int(input())
for _ in range(tc):
    V, E = map(int, input().split())
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    
    # arr 그래프 만들기
    for _ in range(E):
        x1, x2 = map(int, input().split())
        arr[x1][x2] = 1
    S, G = map(int, input().split())


    # 처음 값
    stack = [S]
    visited[S] = 1
    top = 0

    while top != -1:
        for j in range(1, V+1):
            if arr[S][j] == 1 and visited[j] == 0:
                stack.append(j)
                S = j
                top += 1
                visited[j] = 1
                break
        else:
            top -= 1
            S = stack[top]

    if G in stack:
        result.append(1)
    else:
        result.append(0)

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))
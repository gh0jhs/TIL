import sys
sys.stdin = open('input.txt')

def bfs(x):
    visited[x] = 1
    que = []
    que.append(x)
    while que:
        i = que.pop(0)
        for j in range(len(graph)):
            if graph[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                que.append(j)


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    answer = 0
    for i in range(0, len(arr)-1, 2):
        x, y = arr[i], arr[i+1]
        graph[x][y], graph[y][x] = 1, 1
    # print(graph)
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(i)
            answer += 1
    print('#{} {}'.format(tc, answer))
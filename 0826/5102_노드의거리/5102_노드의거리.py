import sys
sys.stdin = open('input.txt')
#
def bfs(data, s, g):
    global visited
    visited[s] = 1
    queue = [s]

    while queue:
        s = queue.pop(0)

        for j in range(v+1):
            if data[s][j] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] += visited[s] + 1
                if j == g:
                    break

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    data = [[0 for _ in range(v+1)] for _ in range(v+1)]
    for i in range(len(arr)):
        x1 = arr[i][0]
        x2 = arr[i][1]
        data[x1][x2] = data[x2][x1] = 1
    visited = [0 for _ in range(v+1)]

    bfs(data, s, g)
    if visited[g] == 0:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, visited[g] - 1))

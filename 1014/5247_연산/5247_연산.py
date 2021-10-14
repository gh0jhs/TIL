import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    visited = [0 for _ in range(2*m)]
    answer = 0
    que = deque()
    que.append([n, visited[n]])
    while que:
        x = que.popleft()
        if x[0] == m:
            answer = x[1]
            break
        for i in [x[0]+1, x[0]-1, x[0]*2, x[0]-10]:
            if 1 <= i <= 2*m and visited[i] == 0:
                visited[i] = visited[x[0]] + 1
                que.append([i, visited[i]])
    print('#{} {}'.format(tc, answer))
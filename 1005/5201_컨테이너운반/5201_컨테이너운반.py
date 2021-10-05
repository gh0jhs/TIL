import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)
    visited = [False] * len(w)

    ans = 0
    for i in range(len(t)):
        for j in range(len(w)):
            if w[j] <= t[i] and visited[j] == False:
                visited[j] = True
                ans += w[j]
                break

    print('#{} {}'.format(tc, ans))
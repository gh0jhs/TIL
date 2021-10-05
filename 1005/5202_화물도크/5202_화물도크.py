import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]

    s_time = sorted(time, key = lambda x: [x[1], x[0]])
    # print(sort_time)

    ans = 0
    end = 0
    for i in range(len(s_time)):
        if s_time[i][0] >= end:
            end = s_time[i][1]
            ans += 1

    print('#{} {}'.format(tc, ans))
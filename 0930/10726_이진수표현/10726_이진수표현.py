import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = 1
    for i in range(N):
        if M & (1 << i) == 0:
            flag = 0
            break

    if flag:
        print('{} {}'.format(tc, 'ON'))
    else:
        print('{} {}'.format(tc, 'OFF'))
import sys
sys.stdin = open('input.txt')
#
for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    cnt = 1
    while data[-1] > 0:
        if cnt == 6:
            cnt = 1
        data.append(data.pop(0) - cnt)
        cnt += 1
    data[-1] = 0
    print('#{} {}'.format(tc, ' '.join(map(str, data))))

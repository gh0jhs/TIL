import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = float(input())
    ans = ''
    for i in range(1, 13):
        if n >= 2**(-i):
            ans += '1'
            n -= 2**(-i)
        else:
            ans += '0'

        if n == 0:
            break

    if n != 0:
        ans = 'overflow'
    print('#{} {}'.format(tc, ans))
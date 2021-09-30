import sys
sys.stdin = open('input.txt')

asc = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

T = int(input())
for tc in range(1, T+1):
    n, my_str = input().split()
    ans = ''
    for i in my_str:
        temp = bin(asc[i])[2:]
        if len(temp) != 4:
            while len(temp) != 4:
                temp = '0' + temp
        ans += temp
    print('#{} {}'.format(tc, ans))
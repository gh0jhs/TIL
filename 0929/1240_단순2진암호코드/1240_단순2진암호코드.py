import sys
sys.stdin = open('input.txt')

asc = {
    '0001101' : '0',
    '0011001' : '1',
    '0010011' : '2',
    '0111101' : '3',
    '0100011' : '4',
    '0110001' : '5',
    '0101111' : '6',
    '0111011' : '7',
    '0110111' : '8',
    '0001011' : '9',
}


T = int(input())
for tc in range(1, T+1):
    ans = ''
    n, m = map(int, input().split())
    arr = [(input()) for _ in range(n)]
    for i in range(len(arr)):
        if '1' in arr[i]:
            temp = arr[i]
            break
    # print(temp)
    for i in range(len(temp)-1, -1, -1):
        if temp[i] == '1':
            idx = i
            break
    # print(idx)
    temp = temp[idx-55:idx+1]
    # print(temp)
    for i in range(8):
        lst = temp[7*i:7*i+7]
        ans += asc[lst]
    # print(ans)
    total = 0
    for i in range(len(ans)):
        if i % 2 == 0:
           total += int(ans[i])
    total *= 3
    for i in range(len(ans)):
        if i % 2 == 1:
            total += int(ans[i])
    answer = 0
    if total % 10 == 0:
        for i in range(len(ans)):
            answer += int(ans[i])
    print('#{} {}'.format(tc, answer))
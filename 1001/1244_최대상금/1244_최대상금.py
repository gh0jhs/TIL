import sys
sys.stdin = open('input.txt')

def perm(n, r, cnt, data):
    if r > n:
        my_set = set()
        for i in range(n):
            for j in range(n):
                temp = ''
                for k in range(len(data)):
                    temp += data[k]
                temp = int(temp)
                my_set.add(temp)
        perm(n, r-n, cnt, list(str(max(my_set))))


    else:
        if cnt == r:
            # print(data)
            temp = ''
            for i in range(len(data)):
                temp += data[i]
            temp = int(temp)
            ans.append(temp)
            return

        for i in range(n):
            for j in range(i + 1, n):
                data[i], data[j] = data[j], data[i]
                perm(n, r, cnt + 1, data)
                data[i], data[j] = data[j], data[i]


T = int(input())
for tc in range(1, T + 1):
    data, r = map(int, input().split())
    data = list(str(data))
    n = len(data)
    ans = []
    perm(n, r, 0, data)
    print('#{} {}'.format(tc, max(ans)))
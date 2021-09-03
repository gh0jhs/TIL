T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if p.count('D') > n:
        arr = input()
        print('error')
    elif p.count('D') == n:
        arr = input()
        print('[]')
    else:
        arr = list(map(int, input()[1:-1].split(',')))
        R_bool = True
        cnt1 = 0
        cnt2 = 0
        for i in p:
            if i == 'R':
                R_bool = not R_bool
            else:
                if R_bool:
                    cnt1 += 1
                else:
                    cnt2 += 1
        if R_bool:
            print('[', end='')
            for i in range(cnt1, n-cnt2-1):
                print(arr[i],end=',')
            print(arr[n-cnt2-1], end='')
            print(']')
        else:
            arr = arr[::-1]
            print('[', end='')
            for i in range(cnt2, n-cnt1-1):
                print(arr[i],end=',')
            print(arr[n-cnt1-1], end='')
            print(']')
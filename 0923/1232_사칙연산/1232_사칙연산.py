import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    # print(arr)
    tree = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        x = arr[i]
        if len(x) == 2:
            tree[int(x[0])] = int(x[1])

        elif len(x) == 4:
            if x[1] == '+':
                tree[int(x[0])] = tree[int(x[2])] + tree[int(x[3])]
            elif x[1] == '-':
                tree[int(x[0])] = tree[int(x[2])] - tree[int(x[3])]
            elif x[1] == '*':
                tree[int(x[0])] = tree[int(x[2])] * tree[int(x[3])]
            elif x[1] == '/':
                tree[int(x[0])] = tree[int(x[2])] / tree[int(x[3])]

    ans = int(tree[1]) # 정수값 반환

    print('#{} {}'.format(tc, ans))
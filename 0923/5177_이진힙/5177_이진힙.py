import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0 for _ in range(n+1)]

    for i in range(1, len(tree)):
        tree[i] = arr[i-1]

        if i == 1:
            continue # tree[0]은 의미없는 값이므로

        while i != 1:
            if tree[i] < tree[i//2]:
                tree[i], tree[i//2] = tree[i//2], tree[i] # 부모값이 더 크면 스왑
            i //= 2

    ans = 0
    while n != 1:
        n //= 2
        ans += tree[n]
    print(tree)
    print('#{} {}'.format(tc, ans))
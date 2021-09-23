import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(m)]
    # print(leaf)
    tree = [0 for _ in range(n+1)]
    for i in range(len(leaf)):
        tree[leaf[i][0]] = leaf[i][1]
    # print(tree)

    for i in range(n, 0, -1):
        if tree[i] != 0:
            continue
        if n < 2*i + 1:
            tree[i] = tree[2*i]
        else:
            tree[i] = tree[2*i] + tree[2*i + 1]
    # print(tree)
    print('#{} {}'.format(tc, tree[l]))
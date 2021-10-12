import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    answer = 100000000
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    comb = list(combinations(list(range(n)), n//2))

    length = len(comb)
    comb_A = comb[:length//2]
    comb_B = comb[length//2:][::-1]

    A_list = []
    B_list = []
    for i in range(len(comb_A)):
        A_list.append(list(combinations(comb_A[i], 2)))
        B_list.append(list(combinations(comb_B[i], 2)))

    for l in range(len(A_list)):
        A = B = 0
        for i in range(len(A_list[l])):
            for j in range(len(A_list[l][i])):
                for k in range(j+1, len(A_list[l][i])):
                    x = A_list[l][i][j]
                    y = A_list[l][i][k]
                    A += arr[x][y] + arr[y][x]
                    u = B_list[l][i][j]
                    v = B_list[l][i][k]
                    B += arr[u][v] + arr[v][u]
        if answer > abs(A-B):
            answer = abs(A-B)
    print('#{} {}'.format(tc, answer))
import sys
sys.stdin = open('input.txt')

from itertools import product
import copy

def check(i, j):
    if 0 <= i < h and 0 <= j < w:
        return True
    return False

def boom(i, j, cnt):
    global answer
    if arr[i][j] == 0:
        return
    arr[i][j] = 0
    answer += 1
    k = 0
    while k != cnt:
        if check(i + k, j):
            if arr[i + k][j] != 0:
                boom(i + k, j, arr[i+k][j])
        if check(i - k, j):
            if arr[i - k][j] != 0:
                boom(i - k, j, arr[i-k][j])
        if check(i, j + k):
            if arr[i][j + k] != 0:
                boom(i, j + k, arr[i][j+k])
        if check(i, j - k):
            if arr[i][j - k] != 0:
                boom(i, j - k, arr[i][j-k])
        k += 1


T = int(input())
for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(h)]
    order = list(product(list(range(w)), repeat=n))
    answer_list = []
    answer = 0
    for i in range(len(order)):
        arr = copy.deepcopy(data)
        answer = 0
        for j in range(len(order[i])):
            x = 0
            y = order[i][j]
            while True:
                if arr[x][y] != 0:
                    break
                else:
                    x += 1
                if x == h:
                    break
            if x == h:
                continue
            boom(x, y, arr[x][y])
            while True:
                change = False
                for i in range(h-1):
                    for j in range(w):
                        if arr[i][j] != 0 and arr[i+1][j] == 0:
                            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                            change = True
                if not change:
                    break
        answer_list.append(answer)
    print(max(answer_list))
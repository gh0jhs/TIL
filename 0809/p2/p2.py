import sys
sys.stdin = open('input.txt')

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input())))
result = []
for i in lst:
    run = 0
    triplet = 0
    cnt =[0] * 10
    for j in i:
        cnt[j] += 1 # 카운트 리스트 만들기
    for k in cnt:
        if k >= 3:
            k -= 3
            triplet += 1
    for k in range(len(cnt)-2):
        if cnt[k] >= 1 and cnt[k+1] >= 1 and cnt[k+2] >= 1:
            run += 1
    if triplet + run == 2:
        result.append('Baby-gin')
    else:
        result.append('X')
for i in result:
    print(i)
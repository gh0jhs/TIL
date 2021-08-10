import sys
sys.stdin = open('input.txt')

n = int(input())
result_i = []
result_cnt = []
for _ in range(n):
    lst = []
    length = int(input())
    string = input()
    lst.extend(string)


    max_cnt = 0
    max_i = 0
    for i in lst:
        cnt = 0
        for j in lst:
            if i == j:
                cnt += 1
        if cnt > max_cnt and int(i) >max_i:
            max_i = int(i)
            max_cnt = cnt
    result_i.append(max_i)
    result_cnt.append(max_cnt)

for i in range(n):
    print('#{} {} {}'.format(i+1, result_i[i], result_cnt[i]))



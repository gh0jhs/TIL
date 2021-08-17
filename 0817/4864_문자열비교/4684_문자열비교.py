import sys
sys.stdin = open('input.txt')

T = int(input())
result = [] # 결과 리스트

# 인풋
for _ in range(T):
    str1 = input()
    str2 = input()
    m = len(str1)
    n = len(str2)
    
    # 브루트포스 알고리즘
    i = 0
    j = 0
    while i < m and j < n:
        if str2[j] != str1[i]:
            j -= i
            i = -1
        j += 1
        i += 1
    if i == m:
        result.append(1)
    else:
        result.append(0)

# 결과 출력
for i in range(T):
    print('#{} {}'.format(i+1, result[i]))
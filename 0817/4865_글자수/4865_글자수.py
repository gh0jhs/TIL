import sys
sys.stdin = open('input.txt')
#
n = int(input())
result = [] # 결과 리스트

# 인풋
for _ in range(n):
    str1 = input()
    str2 = input()

# 최댓값 초기화
    max_temp = 0
    for i in str1: # 글자 하나씩 확인
        if max_temp < str2.count(i):
            max_temp = str2.count(i)
    result.append(max_temp)


# 결과 출력
for i in range(n):
    print('#{} {}'.format(i+1, result[i]))
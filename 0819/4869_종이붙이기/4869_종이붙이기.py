import sys
sys.stdin = open('input.txt')
#
# 점화식
# 1 3 5 11 21
# 짝수 -> 홀수 : 2n-1
# 홀수 -> 짝수 : 2n+1

def recur(n):
    if n == 1:
        return 1
    else:
        if n % 2:
            return 2*recur(n-1) - 1
        else:
            return 2*recur(n-1) + 1

result = []
tc = int(input())
for _ in range(tc):
    n = int(input())
    n = n//10 #인덱스
    result.append(recur(n))

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))



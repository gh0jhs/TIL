import sys
sys.stdin = open('input.txt')

tc = int(input())
result = []
for _ in range(tc):
    val = 0
    n, k = map(int, input().split())
    A = list(range(1, 13)) #1~12 A 집합 생성

    # 모든 부분집합 생성
    for i in range(1<<12):
        lst = []
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                lst.append(A[j])

        # 원소 개수가 n 이고 합이 k인 경우
        if len(lst) == n and sum(lst) == k:
            val += 1
    result.append(val)
    
#프린트
for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))
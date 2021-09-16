import sys
sys.stdin = open('input.txt')

##  탐색
def binary_search(start, end, target, cnt): # 파라미터 카운트
    while start <= end:
        cnt += 1
        mid = int((start + end) / 2)

        if mid == target:
            break
        elif mid < target:
            start = mid # + 1???
        else:
            end = mid # - 1???

    return cnt

# 입력
T = int(input())
result = []
for _ in range(T):
    n, p_a, p_b = map(int, input().split())


    # 값들 초기화
    cnt_a = 0
    cnt_b = 0
    start = 1
    end = n
    cnt_a = binary_search(start, end, p_a, cnt_a)
    cnt_b = binary_search(start, end, p_b, cnt_b)


    if cnt_a < cnt_b:
        result.append('A')
    elif cnt_a > cnt_b:
        result.append('B')
    else:
        result.append(0)

# 프린트

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))
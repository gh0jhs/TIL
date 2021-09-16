import sys
sys.stdin = open('input.txt')
#
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n: 화덕의 크기, m: 피자 갯수
    arr = list(map(int, input().split()))
    queue = []

    for i in range(n):
        queue.append([i+1, arr[i]]) # 큐에 피자를 화덕의 크기만큼 추가(피자 번호와 함께 추가)
    idx = n # 다음 넣어줄 피자의 인덱스
    while len(queue) != 1: # 피자가 하나남을때까지 while
        x = queue.pop(0)
        x[1] = x[1] // 2
        if x[1] == 0:
            if idx != m: # 피자 갯수넘지 않을 때 
                queue.append([idx+1, arr[idx]]) # 큐에 피자 추가
                idx += 1
        else:
            queue.append(x)
    print('#{} {}'.format(tc, queue[0][0]))
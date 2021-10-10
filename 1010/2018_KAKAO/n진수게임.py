def solution(n, t, m, p):
    answer = ''
    game ='0'
    dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    for i in range(1, t*m):
        num = ''
        if i < n:
            if i >= 10:
                game += dict[i]
            else:
                game += str(i)
        else:
            while i >= n:
                if i % n >= 10:
                    num = dict[i % n] + num
                else:
                    num = str(i % n) + num
                i //= n
            if i >= 10:
                num = dict[i] + num
            else:
                num = str(i) + num
            game += num
    cnt = 0
    for i in range(len(game)):
        cnt += 1
        if cnt == p:
            answer += game[i]
        if cnt == m:
            cnt = 0
        if len(answer) == t:
            break
    return answer